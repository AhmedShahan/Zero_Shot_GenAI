from transformers import pipeline

# Load Whisper model
whisper = pipeline("automatic-speech-recognition", model="openai/whisper-large")
