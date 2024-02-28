from enum import Enum


class ExperimentAction(str, Enum):
    TRAIN = "train"
    EVALUATE = "evaluate"
    EXPORT = "export"
    GEN_TRT_ENGINE = "gen_trt_engine"
    INFERENCE = "inference"
    PRUNE = "prune"
    RETRAIN = "retrain"
    CONFMAT = "confmat"


class ConvertAction(str, Enum):
    DATASET_CONVERT = "dataset_convert"
    CONVERT = "convert"
    CONVERT_AND_INDEX = "convert_and_index"
    CONVERT_EFFICIENTDET_TF1 = "convert_efficientdet_tf1"
    CONVERT_EFFICIENTDET_TF2 = "convert_efficientdet_tf2"
    CONVERT_AUGMENT = "augment"
    CONVERT_KMEANS = "kmeans"