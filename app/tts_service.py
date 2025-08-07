from TTS.api import TTS
from pathlib import Path
import uuid

# Load model once at startup
MODEL_PATH = "models/ewe_vits.pth"
CONFIG_PATH = "config/ewe_config.json"

tts = TTS(model_path=MODEL_PATH, config_path=CONFIG_PATH, progress_bar=False, gpu=True)

def generate_tts(text: str) -> str:
    output_path = f"/tmp/{uuid.uuid4()}.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path
