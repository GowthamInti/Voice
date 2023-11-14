import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
CUDA_IS_AVAILABLE = DEVICE == "cuda"

def wavfile(file_path):
    with open(file_path, "rb") as wav_file:
        wav_data = wav_file.read()
    return wav_data