import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def read_wav(file_path):
    # Reading the wav file
    sample_rate, data = wavfile.read(file_path)
    return sample_rate, data

def plot_channels(data, sample_rate, max_voltage=24.11345):
    num_channels = data.shape[1] if len(data.shape) > 1 else 1
    time = np.arange(0, len(data)) / sample_rate

    plt.figure(figsize=(12, 6))
    for i in range(num_channels):
        channel_data = data[:, i] if num_channels > 1 else data
        # Normalizing the data to the maximum voltage
        channel_data = channel_data / np.max(np.abs(channel_data)) * max_voltage

        plt.subplot(num_channels, 1, i + 1)
        plt.plot(time, channel_data)
        plt.title(f'Channel {i + 1}')
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [V]')
        plt.grid()

    plt.tight_layout()
    plt.show()

# Replace 'your_file.wav' with the path to your .wav file
file_path = '24vamp_sine_input.wav'
sample_rate, data = read_wav(file_path)
plot_channels(data, sample_rate)
