import numpy as np
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2Model
import librosa
import torchaudio
  # Replace with your augmentation imports

# Load the Wav2Vec2 model and processor
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "jonatasgrosman/wav2vec2-large-xlsr-53-english"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2Model.from_pretrained(model_name).to(device)

embedding_size = 512




# The feature extraction function as provided
def extract_wav2vec2_features(filepath, fonction_augmentation=None):
    speech_array, sampling_rate = torchaudio.load(filepath)
    speech_array = speech_array.squeeze().numpy()

    # Apply augmentation if provided
    if fonction_augmentation:
        speech_array = fonction_augmentation(speech_array, sampling_rate)

    # Resample to 16kHz if needed
    if sampling_rate != 16000:
        speech_array = librosa.resample(speech_array, orig_sr=sampling_rate, target_sr=16000)

    # Use processor to extract the embeddings
    inputs = processor(speech_array, sampling_rate=16000, return_tensors="pt", padding=True)
    input_values = inputs.input_values.to(device)
    attention_mask = inputs.attention_mask.to(device)

    with torch.no_grad():
        output = model(input_values, attention_mask=attention_mask)

    # Average pooling across time dimension to get final feature vector
    embeddings = output.extract_features.squeeze(0).cpu().numpy()
    mean_embedding = np.mean(embeddings, axis=0)
    return mean_embedding
