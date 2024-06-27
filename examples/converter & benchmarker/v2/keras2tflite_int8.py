from netspresso import NetsPresso
from netspresso.enums import DataType, DeviceName, Framework

# Available target frameworks for conversion with keras models
#
# Framework.TENSORFLOW_LITE
#

# Available devices for Framework.TENSORFLOW_LITE and DataType.INT8 (target_framework)
#
# DeviceName.RASPBERRY_PI_4B
# DeviceName.RASPBERRY_PI_3B_PLUS
# DeviceName.RASPBERRY_PI_ZERO_W
# DeviceName.RASPBERRY_PI_ZERO_2W
# DeviceName.ALIF_ENSEMBLE_E7_DEVKIT_GEN2
# DeviceName.RENESAS_RA8D1
#

EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

netspresso = NetsPresso(email=EMAIL, password=PASSWORD)

# 1. Declare converter
converter = netspresso.converter_v2()

# 2. Set variables for convert
INPUT_MODEL_PATH = "./examples/sample_models/mobilenetv1_cifar100_automatic.h5"
OUTPUT_DIR = "./outputs/converted/TFLITE_INT8_RENESAS_RA8D1"
TARGET_FRAMEWORK = Framework.TENSORFLOW_LITE
TARGET_DEVICE_NAME = DeviceName.RENESAS_RA8D1
TARGET_DATA_TYPE = DataType.INT8
DATASET_PATH = "./examples/sample_datasets/20x32x32x3.npy"

# 3. Run convert
conversion_task = converter.convert_model(
    input_model_path=INPUT_MODEL_PATH,
    output_dir=OUTPUT_DIR,
    target_framework=TARGET_FRAMEWORK,
    target_data_type=TARGET_DATA_TYPE,
    target_device_name=TARGET_DEVICE_NAME,
    dataset_path=DATASET_PATH,
)
print(conversion_task)

# 4. Declare benchmarker
benchmarker = netspresso.benchmarker_v2()

# 5. Run benchmark
benchmark_task = benchmarker.benchmark_model(
    input_model_path=conversion_task.converted_model_path,
    target_device_name=TARGET_DEVICE_NAME,
)
print(f"model inference latency: {benchmark_task.benchmark_result.latency} ms")
