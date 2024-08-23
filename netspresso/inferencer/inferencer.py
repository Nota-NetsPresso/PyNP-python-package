import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
import cv2
import numpy as np
from netspresso_inference_package.inference.inference_service import InferenceService
from omegaconf import OmegaConf
from loguru import logger

from netspresso.inferencer.preprocessors.base import Preprocessor
from netspresso.inferencer.postprocessors.detection import DetectionPostprocessor
from netspresso.inferencer.postprocessors.classification import ClassificationPostprocessor
from netspresso.inferencer.postprocessors.segmentation import SegmentationPostprocessor
from netspresso.inferencer.visualizers.classification import ClassificationVisualizer
from netspresso.inferencer.visualizers.detection import DetectionVisualizer
from netspresso.inferencer.visualizers.segmentation import SegmentationVisualizer
from netspresso.enums import Runtime, Task


class BaseInferencer:
    def __init__(self) -> None:
        pass

    def _inference(self, input_model_path: str, dataset_path: str):
        inf_service = InferenceService(model_file_path=input_model_path, dataset_file_path=dataset_path)
        inference_results = inf_service.inference()

        return inference_results

    def transpose_input(self, runtime, input):
        if runtime == Runtime.ONNX:
            input = input.transpose(0, 3, 1, 2)
        elif runtime == Runtime.TFLITE:
            pass

        return input

    def transpose_outputs(self, runtime, outputs):
        if runtime == Runtime.ONNX:
            pass
        elif runtime == Runtime.TFLITE:
            outputs = [np.transpose(index, (0, 3, 1, 2)) for index in outputs] # (b, h, w, c) -> (b, c, h, w)

        return outputs

    def save_numpy_data(self, data):
        with tempfile.NamedTemporaryFile(suffix=".npy", delete=False) as temp_file:
            save_path = temp_file.name
            np.save(save_path, data)

        return save_path

    def save_image(self, image, save_path):
        save_path = Path(save_path)

        if not save_path.parent.exists():
            save_path.parent.mkdir(parents=True, exist_ok=True)
            logger.info(f"The folder has been created. Local Path: {save_path.parent}")

        cv2.imwrite(save_path.as_posix(), cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        logger.info(f"Result image saved at {save_path}.")

        return save_path.as_posix()


class NPInferencer(BaseInferencer):
    def __init__(self, config_path) -> None:
        super().__init__()
        self.config_path = config_path
        self.runtime_config = OmegaConf.load(config_path).runtime
        self.build_preprocessor()
        self.build_postprocessor()
        self.build_visualizer()

    def build_preprocessor(self):
        self.preprocessor = Preprocessor(self.runtime_config.preprocess)

    def build_postprocessor(self):
        if self.runtime_config.task == Task.IMAGE_CLASSIFICATION:
            self.postprocessor = ClassificationPostprocessor()
        elif self.runtime_config.task == Task.OBJECT_DETECTION:
            params = self.runtime_config.postprocess.params
            del params.class_agnostic
            self.postprocessor = DetectionPostprocessor(**params)
        elif self.runtime_config.task == Task.SEMANTIC_SEGMENTATION:
            self.postprocessor = SegmentationPostprocessor()

    def build_visualizer(self):
        params = self.runtime_config.visualize.params
        if self.runtime_config.task == Task.IMAGE_CLASSIFICATION:
            self.visualizer = ClassificationVisualizer(**params)
        if self.runtime_config.task == Task.OBJECT_DETECTION:
            self.visualizer = DetectionVisualizer(**params)
        if self.runtime_config.task == Task.SEMANTIC_SEGMENTATION:
            self.visualizer = SegmentationVisualizer(**params)

    def inference(self, input_model_path: str, image_path: str, save_path: str):
        suffix = Path(input_model_path).suffix
        runtime = Runtime.get_runtime_by_suffix(suffix)

        # Load image
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_draw = img.copy()

        # Preprocess image
        img = self.preprocessor(img)
        input_data = self.transpose_input(runtime=runtime, input=img)
        dataset_path = self.save_numpy_data(data=input_data)

        # Inference data
        inference_results = self._inference(input_model_path, dataset_path)
        Path(dataset_path).unlink()

        # Postprocess outputs
        outputs = [value for value in inference_results.values()]
        outputs = self.transpose_outputs(runtime, outputs)
        model_input_shape = None

        if self.runtime_config.task == Task.IMAGE_CLASSIFICATION:
            pred = self.postprocessor({"pred": outputs[0]}, k=1)[0]
        
        elif self.runtime_config.task == Task.OBJECT_DETECTION:
            model_input_shape = img.shape[1:3]
            pred = self.postprocessor({"pred": outputs}, model_input_shape)[0]
        elif self.runtime_config.task == Task.SEMANTIC_SEGMENTATION:
            model_input_shape = img.shape[1:3]
            pred = self.postprocessor({"pred": outputs[0]}, model_input_shape)
        import ipdb; ipdb.set_trace()

        # Draw outputs
        img_draw = self.visualizer.draw(image=img_draw, pred=pred, model_input_shape=model_input_shape)

        self.save_image(image=img_draw, save_path=save_path)

        return img_draw


class CustomInferencer(BaseInferencer):
    def __init__(self) -> None:
        super().__init__()

    def inference(self, input_model_path: str, dataset_path: str):
        suffix = Path(input_model_path).suffix
        runtime = Runtime.get_runtime_by_suffix(suffix)

        inference_results = self._inference(input_model_path, dataset_path)

        outputs = [value for value in inference_results.values()]
        outputs = self.transpose_outputs(runtime, outputs)

        return outputs
