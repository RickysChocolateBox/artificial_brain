import numpy as np
import scipy.signal as signal

def preprocess_humidity_data(data):
    # Apply low-pass filter to remove noise and smooth the signal
    b, a = signal.butter(4, 0.1, btype='lowpass', fs=data['sampling_rate'])
    filtered = signal.filtfilt(b, a, data['humidity'])
    # Calculate statistics such as mean and variance
    mean = np.mean(filtered)
    std = np.std(filtered)
    max_val = np.max(filtered)
    min_val = np.min(filtered)
    # Calculate additional features such as rate of change and variance of differences
    diff = np.diff(filtered)
    roc = np.mean(np.abs(diff))
    diff_var = np.var(diff)
    # Return preprocessed data
    return {'mean': mean, 'std': std, 'max_val': max_val, 'min_val': min_val, 'roc': roc, 'diff_var': diff_var}
