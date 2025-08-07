from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from app.tts_service import generate_tts

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Ewe TTS API"}

@app.get("/speak")
def speak(text: str = Query(..., min_length=1)):
    output_path = generate_tts(text)
    return FileResponse(output_path, media_type="audio/wav", filename="speech.wav")
