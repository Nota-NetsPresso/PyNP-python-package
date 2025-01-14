from enum import Enum


class SubFolder(str, Enum):
    TRAINED_MODELS = "trained_models"
    COMPRESSED_MODELS = "compressed_models"
    PRETRAINED_MODELS = "pretrained_models"
