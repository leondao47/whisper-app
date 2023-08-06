import time
import uuid
import os

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import whisper_timestamped as whisper

# Init Whisper
model = whisper.load_model("tiny.en", device="cpu")

app = Flask(__name__)
CORS(app)

@app.route("/")
def serve_index():
    return send_file("../fe/index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    start = time.time()
    if 'audio' not in request.files:
        return jsonify({'message': 'No audio part in the request'}), 400

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'message': 'No selected audio file'}), 400

    # Save the audio file to the desired location (change 'uploads' to your preferred directory)
    save_file_name = f'{audio_file.filename}_{uuid.uuid4()}'
    audio_file.save(save_file_name)
    audio = whisper.load_audio(save_file_name)
    result = whisper.transcribe(model, audio)
    os.remove(f'{save_file_name}')

    print(f'time: {time.time() - start}')
    return jsonify({'message': 'Audio uploaded successfully!', 'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)