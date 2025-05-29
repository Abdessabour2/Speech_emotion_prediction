import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import logging
logging.getLogger('absl').setLevel(logging.ERROR)
from flask import Flask, request, jsonify, render_template
import os
import numpy as np
import librosa
import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2Model
import tensorflow as tf
from processing import extract_wav2vec2_features
app = Flask(__name__)
model = tf.keras.models.load_model('model\emotion_model_final.h5') 
processor = Wav2Vec2Model.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if file is part of the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        file_path = file.filename
        file.save(file_path)
        features = extract_wav2vec2_features(file_path)
        features = np.reshape(features, (1, -1))
        prediction = model.predict(features)
        labels = ['Angry' ,'Disgusted' ,'Fearful' ,'Happy' ,'Neutral' ,'Sad' ,'Suprised']
        predicted_label = labels[np.argmax(prediction)]
        return jsonify({"prediction": predicted_label})    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
