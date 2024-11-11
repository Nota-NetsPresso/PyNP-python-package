from pathlib import Path

from netspresso import NetsPresso
from netspresso.enums import QuantizationPrecision
from netspresso.quantizer.quantizer import PrecisionByLayer
from netspresso.utils.file import FileHandler


EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

netspresso = NetsPresso(email=EMAIL, password=PASSWORD)


# 1. Declare quantizer
quantizer = netspresso.quantizer()

# 2. Set variables for quantize
input_model = "./examples/sample_models/test.onnx"
OUTPUT_DIR = "./outputs/quantized/onnx2onnx_2"
CALIBRATION_DATASET_PATH = "./examples/sample_datasets/pickle_calibration_dataset_128x128.npy"

# 3-1. Recommendation precision
recommendation_metadata = quantizer.get_recommendation_precision(
    input_model_path=input_model,
    output_dir=f"{OUTPUT_DIR}/{Path(input_model).stem}",
    dataset_path=CALIBRATION_DATASET_PATH,
    weight_precision=QuantizationPrecision.INT8,
    activation_precision=QuantizationPrecision.INT8,
    threshold=0,
)

recommendation_result = FileHandler.load_json(file_path=recommendation_metadata.recommendation_result_path)
layers = recommendation_result["layers"]
precision_by_layer_name = [
    PrecisionByLayer(
        name=layer["name"],
        precision=layer["recommendation"]["precision"][0],
    )
    for layer in layers
]

# 3-2. Custom Quantization
quantizer.custom_quantization_by_layer_name(
    input_model_path=input_model,
    output_dir=f"{OUTPUT_DIR}/{Path(input_model).stem}",
    precision_by_layer_name=precision_by_layer_name,
    dataset_path=CALIBRATION_DATASET_PATH,
)
