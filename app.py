from flask import Flask, request, jsonify, render_template, send_from_directory, send_file
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioConfig, ResultReason, SpeechSynthesisCancellationDetails, CancellationReason
import json
import uuid
import os
import configparser
from datetime import datetime

try:
    from google import genai  # Import the Gemini AI client library
except ImportError:
    raise ImportError("Please install the google-genai package")

# Load API keys from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
subscription_key = config.get('API_KEYS', 'azure_subscription_key')
region = config.get('API_KEYS', 'azure_region')
gemini_api_key = config.get('API_KEYS', 'gemini_api_key')

# Initialize the Gemini client with your API key
client = genai.Client(api_key=gemini_api_key)

app = Flask(__name__)

USER_CONTEXT_FILE = "user_context.json"
CONVERSATIONS_FILE = "conversations.json"

# Initialize the SpeechConfig with your Azure subscription key and region
speech_config = SpeechConfig(subscription=subscription_key, region=region)

# Load user context from a JSON file
def load_user_context():
    try:
        with open(USER_CONTEXT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save user context to a JSON file
def save_user_context(context):
    with open(USER_CONTEXT_FILE, "w") as f:
        json.dump(context, f, indent=4)

# Load conversations from a JSON file
def load_conversations():
    try:
        with open(CONVERSATIONS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save conversations to a JSON file
def save_conversations(conversations):
    with open(CONVERSATIONS_FILE, "w") as f:
        json.dump(conversations, f, indent=4)

# Speech synthesis function
def synthesize_speech(text, voice_name="zu-ZA-ThandoNeural", pitch="0%", rate="1.0"):
    output_filename = str(uuid.uuid4()) + ".wav"
    audio_config = AudioConfig(filename=output_filename)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    ssml_text = f"""
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='{voice_name[:5]}'>
        <voice name='{voice_name}'>
            <prosody pitch='{pitch}' rate='{rate}'>
                {text}
            </prosody>
        </voice>
    </speak>
    """

    result = synthesizer.speak_ssml_async(ssml_text).get()

    if result.reason == ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesis succeeded. Audio saved to {output_filename}")
        return jsonify({'status': 'Speech synthesis complete', 'audio_file': output_filename})
    elif result.reason == ResultReason.Canceled:
        cancellation_details = SpeechSynthesisCancellationDetails(result)
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            return jsonify({'status': 'Speech synthesis failed', 'error': str(cancellation_details.error_details)}), 500
        return jsonify({'status': 'Speech synthesis failed', 'reason': str(cancellation_details.reason)}), 500
    else:
        return jsonify({'status': 'Speech synthesis failed', 'reason': str(result.reason)}), 500

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(directory=".", path=filename)

class ConversationManager:
    def __init__(self):
        self.memory = []

    def generate_response(self, text):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=text
            )
            return response.text
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Error generating response. Please check the API key and try again."

    def add_to_memory(self, user_input, bot_response):
        self.memory.append(f"User: {user_input}")
        self.memory.append(f"Bot: {bot_response}")

    def analyze_conversation(self, conversation_text, context):
        recommendations = (
            "Based on the provided conversation, here are some recommendations to improve human connections and communication:\n"
            "- Encourage regular and open communication.\n"
            "- Foster a supportive and empathetic environment.\n"
            "- Promote face-to-face interactions and reduce excessive screen time.\n"
            "- Create opportunities for social engagement and community activities.\n"
            "- Address any underlying issues that may hinder effective communication."
        )
        return recommendations

    def adjust_tone(self, message, tone):
        adjusted_message = f"Rewrite the following message in a {tone} tone:\n\n{message}"
        response = self.generate_response(adjusted_message)
        return response

    def analyze_text_conversation(self, conversation_text):
        analysis = self.generate_response(f"Analyze the following conversation:\n\n{conversation_text}")
        return analysis

    def save_conversation(self, user_input, bot_response):
        conversations = load_conversations()
        conversations.append({"user_input": user_input, "bot_response": bot_response})
        save_conversations(conversations)

conversation_manager = ConversationManager()

@app.route('/', methods=['GET'])
def index():
    context = load_user_context()
    return render_template('index.html', context=context)

@app.route('/generate', methods=['POST'])
def generate_content_route():
    data = request.json
    user_input = data['input']
    context = load_user_context()
    if "meeting" in user_input.lower():
        context["last_interaction_type"] = "meeting"
    elif "follow-up" in user_input.lower():
        context["last_interaction_type"] = "follow-up"
    save_user_context(context)
    response_text = conversation_manager.generate_response(user_input)
    conversation_manager.add_to_memory(user_input, response_text)
    conversation_manager.save_conversation(user_input, response_text)
    save_user_context(context)  # Ensure the context is saved after updating
    return jsonify({'response': response_text, 'context': context})

@app.route('/synthesize', methods=['POST'])
def synthesize_route():
    data = request.json
    text = data['text']
    voice_name = data.get('voice_name', "zu-ZA-ThandoNeural")
    pitch = data.get('pitch', "0%")  # Default pitch
    rate = data.get('rate', "1.0")   # Default rate

    try:
        response = synthesize_speech(text, voice_name, pitch, rate)
        return response
    except Exception as e:
        print(f"Error during speech synthesis: {e}")
        return jsonify({'status': 'Speech synthesis failed', 'error': str(e)}), 500

@app.route('/preview_voice', methods=['POST'])
def preview_voice():
    data = request.json
    text = data.get('text', "This is a preview of the current voice settings.")
    voice_name = data.get('voice_name', "zu-ZA-ThandoNeural")
    pitch = data.get('pitch', "0%")
    rate = data.get('rate', "1.0")

    try:
        response = synthesize_speech(text, voice_name, pitch, rate)
        return response
    except Exception as e:
        print(f"Error during voice preview: {e}")
        return jsonify({'status': 'Voice preview failed', 'error': str(e)}), 500

@app.route('/clear_conversation', methods=['POST'])
def clear_conversation():
    conversation_manager.memory = []
    save_conversations([])
    return jsonify({'status': 'Conversation cleared'})

@app.route('/download_conversation', methods=['GET'])
def download_conversation():
    conversations = load_conversations()
    conversation_text = "\n".join([f"User: {conv['user_input']}\nBot: {conv['bot_response']}\n" for conv in conversations])
    filename = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(conversation_text)
    return send_file(filename, as_attachment=True)

@app.route('/analyze', methods=['POST'])
def analyze_content():
    data = request.json
    conversation_text = data['conversation']
    context = load_user_context()
    recommendations = conversation_manager.analyze_conversation(conversation_text, context)
    save_user_context(context)  # Ensure the context is saved after analysis
    return jsonify({'recommendations': recommendations, 'context': context})

@app.route('/tone', methods=['POST'])
def change_tone():
    data = request.json
    message = data['message']
    tone = data['tone']
    adjusted_message = conversation_manager.adjust_tone(message, tone)
    return jsonify({'adjusted_message': adjusted_message})

@app.route('/analyze_conversation', methods=['POST'])
def analyze_conversation():
    data = request.json
    conversation_text = data['conversation_text']
    analysis = conversation_manager.analyze_text_conversation(conversation_text)
    return jsonify({'analysis': analysis})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)