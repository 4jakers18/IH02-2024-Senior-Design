import wave
import numpy as np
import matplotlib.pyplot as plt

def plot_wave(file_name):
    # Open the WAV file
    with wave.open(file_name, 'r') as wav_file:
        # Extract Raw Audio from WAV File
        signal = wav_file.readframes(-1)
        signal = np.frombuffer(signal, dtype='int16')

        # Get the frame rate
        frame_rate = wav_file.getframerate()

        # Time axis in seconds
        time = np.linspace(0, len(signal) / frame_rate, num=len(signal))

        # Plotting the waveform
        plt.figure(figsize=(12, 4))
        plt.plot(time, signal)
        plt.title(f"Waveform of {file_name}")
        plt.ylabel("Amplitude")
        plt.xlabel("Time (s)")
        plt.show()

# Replace 'example.wav' with the path to your WAV file
plot_wave('CantinaBand3.wav')
