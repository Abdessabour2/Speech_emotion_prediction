import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import logging
logging.getLogger('absl').setLevel(logging.ERROR)
import numpy as np
import librosa
import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2Model

import tensorflow as tf
from processing import extract_wav2vec2_features
model = tf.keras.models.load_model('model\emotion_model.h5')  # Update with the correct model path

# Wav2Vec2 processor and model (assuming you're using a Hugging Face Wav2Vec2 model)
# processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
features = extract_wav2vec2_features('angry_example.wav')
features = np.reshape(features, (1, -1))
prediction = model.predict(features)
print(prediction)
labels = ['Angry' ,'Disgusted' ,'Fearful' ,'Happy' ,'Neutral' ,'Sad' ,'Suprised']
predicted_label = labels[np.argmax(prediction)]
print(predicted_label)

