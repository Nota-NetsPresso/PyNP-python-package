from netspresso import NetsPresso

EMAIL = "compressor@nota.ai"
PASSWORD = "Nota180928!"

netspresso = NetsPresso(email=EMAIL, password=PASSWORD)

# 1. Declare compressor
compressor = netspresso.compressor_v2()

# 2. Set variables for compression
INPUT_SHAPES = [{"batch": 1, "channel": 3, "dimension": [224, 224]}]
INPUT_MODEL_PATH = "./examples/sample_models/graphmodule.pt"
OUTPUT_DIR = "./outputs/compressed/pytorch_automatic_compression_1"
COMPRESSION_RATIO = 0.5

# 3. Run automatic compression
compression_result = compressor.automatic_compression(
    input_shapes=INPUT_SHAPES,
    input_model_path=INPUT_MODEL_PATH,
    output_dir=OUTPUT_DIR,
    compression_ratio=COMPRESSION_RATIO,
)
