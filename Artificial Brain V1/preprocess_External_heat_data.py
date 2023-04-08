import numpy as np
import scipy.signal as signal

def preprocess_external_temperature_data(data):
    # Apply low-pass filter to remove noise and smooth the signal
    b, a = signal.butter(4, 0.1, btype='lowpass', fs=data['sampling_rate'])
    filtered = signal.filtfilt(b, a, data['temperature'])
    # Calculate statistics such as mean and variance
    mean = np.mean(filtered)
    std = np.std(filtered)
    max_val = np.max(filtered)
    min_val = np.min(filtered)
    # Return preprocessed data
    return {'mean': mean, 'std': std, 'max_val': max_val, 'min_val': min_val}
