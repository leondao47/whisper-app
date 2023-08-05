import time
import uuid
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper_timestamped as whisper

# Init Whisper
model = whisper.load_model("tiny.en", device="cpu")

app = Flask(__name__)
CORS(app)


# Endpoint to receive audio file via POST request
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return jsonify({'message': 'No audio part in the request'}), 400

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'message': 'No selected audio file'}), 400

    # Save the audio file to the desired location (change 'uploads' to your preferred directory)
    save_file_name = f'{audio_file.filename}_{uuid.uuid4()}'
    audio_file.save('uploads/' + save_file_name)
    audio = whisper.load_audio('uploads/' + save_file_name)
    result = whisper.transcribe(model, audio)
    os.remove(f'uploads/{save_file_name}')

    return jsonify({'message': 'Audio uploaded successfully!', 'result': result}), 200


if __name__ == '__main__':
    app.run(debug=True)
