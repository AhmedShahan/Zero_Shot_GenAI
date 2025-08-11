from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
# import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa
import requests
import os
from dotenv import load_dotenv
import tempfile
import numpy as np
from urllib.parse import urlparse
import soundfile as sf

load_dotenv()

app = Flask(__name__)

# Initialize clients
twilio_client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
# genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

class WhatsAppCallAgent:
    def __init__(self):
        self.conversation_history = {}
        # Initialize Whisper model (this will download on first use)
        print("Loading Whisper model...")
        self.whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-base")
        self.whisper_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")
        print("Whisper model loaded successfully!")
        
        # Initialize Gemini model
        self.gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    
    def transcribe_audio(self, audio_url):
        """Convert speech to text using OpenAI Whisper (Transformers)"""
        try:
            print(f"Transcribing audio from: {audio_url}")
            
            # Download audio file
            response = requests.get(audio_url)
            if response.status_code != 200:
                print(f"Failed to download audio: {response.status_code}")
                return None
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
                temp_file.write(response.content)
                temp_audio_path = temp_file.name
            
            try:
                # Load and preprocess audio
                audio_data, sample_rate = librosa.load(temp_audio_path, sr=16000)
                
                # Process with Whisper
                inputs = self.whisper_processor(
                    audio_data, 
                    sampling_rate=16000, 
                    return_tensors="pt"
                )
                
                # Generate transcription
                with torch.no_grad():
                    predicted_ids = self.whisper_model.generate(inputs["input_features"])
                
                # Decode transcription
                transcription = self.whisper_processor.batch_decode(
                    predicted_ids, 
                    skip_special_tokens=True
                )[0]
                
                print(f"Transcription: {transcription}")
                return transcription.strip()
                
            finally:
                # Clean up temporary file
                if os.path.exists(temp_audio_path):
                    os.unlink(temp_audio_path)
                    
        except Exception as e:
            print(f"Transcription error: {e}")
            return None
    
    def generate_ai_response(self, user_input, caller_id):
        """Generate AI response using Google Gemini"""
        try:
            # Get conversation history
            history = self.conversation_history.get(caller_id, [])
            
            # Build context from history
            context = ""
            if history:
                context = "Previous conversation:\n"
                for msg in history[-5:]:  # Last 5 messages for context
                    role = "User" if msg["role"] == "user" else "Assistant"
                    context += f"{role}: {msg['content']}\n"
                context += "\n"
            
            # Create prompt for Gemini
            prompt = f"""{context}You are a helpful WhatsApp call assistant. Keep responses concise (1-2 sentences), conversational, and friendly. 

User's current message: {user_input}

Response:"""
            
            # Generate response with Gemini
            response = self.gemini_model.generate_content(prompt)
            ai_response = response.text.strip()
            
            # Update conversation history
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": ai_response})
            self.conversation_history[caller_id] = history[-10:]  # Keep last 10 messages
            
            print(f"AI Response: {ai_response}")
            return ai_response
            
        except Exception as e:
            print(f"AI response error: {e}")
            return "I'm sorry, I'm having trouble processing your request right now. Could you please try again?"
    
    def text_to_speech(self, text):
        """Convert text to speech using ElevenLabs"""
        try:
            url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"  # Default voice
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": os.getenv('ELEVENLABS_API_KEY')
            }
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }
            
            response = requests.post(url, json=data, headers=headers)
            
            if response.status_code == 200:
                # Save audio to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
                    f.write(response.content)
                    return f.name
            else:
                print(f"TTS error: {response.status_code}")
                return None
        except Exception as e:
            print(f"TTS error: {e}")
            return None

# Initialize agent (this will load Whisper model)
print("Initializing WhatsApp Call Agent...")
agent = WhatsAppCallAgent()
print("Agent initialized successfully!")

@app.route('/webhook/voice', methods=['POST'])
def handle_voice_call():
    """Handle incoming voice calls"""
    response = VoiceResponse()
    
    # Greet the caller
    response.say("Hello! I'm your AI assistant powered by Gemini. Please speak your message after the beep, and I'll respond to you.")
    
    # Record the caller's message
    response.record(
        max_length=30,
        action='/webhook/process_recording',
        method='POST',
        play_beep=True,
        transcribe=True  # Enable Twilio transcription as backup
    )
    
    return str(response)

@app.route('/webhook/process_recording', methods=['POST'])
def process_recording():
    """Process the recorded audio"""
    response = VoiceResponse()
    
    # Get recording URL and caller ID
    recording_url = request.form.get('RecordingUrl')
    caller_id = request.form.get('From')
    twilio_transcription = request.form.get('TranscriptionText', '').strip()
    
    print(f"Processing recording for caller: {caller_id}")
    print(f"Twilio transcription: {twilio_transcription}")
    
    if recording_url:
        # Use Whisper for transcription
        whisper_transcription = agent.transcribe_audio(recording_url)
        
        # Use Whisper transcription if available, otherwise fall back to Twilio
        transcription = whisper_transcription if whisper_transcription else twilio_transcription
        
        if transcription:
            print(f"Using transcription: {transcription}")
            
            # Generate AI response with Gemini
            ai_response = agent.generate_ai_response(transcription, caller_id)
            
            # Respond with voice
            response.say(ai_response, voice='Polly.Joanna')
            
            # Ask if they want to continue
            response.say("Is there anything else I can help you with?")
            response.record(
                max_length=30,
                action='/webhook/process_recording',
                method='POST',
                play_beep=True,
                transcribe=True
            )
        else:
            response.say("I'm sorry, I couldn't understand what you said. Please speak clearly and try again.")
            response.record(
                max_length=30,
                action='/webhook/process_recording',
                method='POST',
                play_beep=True,
                transcribe=True
            )
    else:
        response.say("I didn't receive your message. Please try calling again.")
        response.hangup()
    
    return str(response)

@app.route('/webhook/status', methods=['POST'])
def call_status():
    """Handle call status updates"""
    call_status = request.form.get('CallStatus')
    caller_id = request.form.get('From')
    
    print(f"Call status for {caller_id}: {call_status}")
    
    if call_status == 'completed':
        # Clean up conversation history if needed
        if caller_id in agent.conversation_history:
            print(f"Cleaning up conversation history for {caller_id}")
            del agent.conversation_history[caller_id]
    
    return '', 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return {'status': 'healthy', 'whisper_loaded': True, 'gemini_configured': True}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)