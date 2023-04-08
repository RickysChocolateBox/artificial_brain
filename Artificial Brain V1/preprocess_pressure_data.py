import numpy as np
from scipy import signal

def preprocess_pressure_data(data):
    # Apply high-pass filter to remove baseline drift
    filtered = signal.sosfilt(signal.butter(4, 0.01, btype='highpass', fs=data['sampling_rate'], output='sos'), data)
    # Calculate statistics such as mean and variance
    mean = np.mean(filtered)
    std = np.std(filtered)
    max_val = np.max(filtered)
    min_val = np.min(filtered)
    # Extract features such as pressure distribution and symmetry
    distribution, _ = np.histogram(filtered, bins=10)
    symmetry = np.abs(np.sum(filtered[:filtered.size//2]) - np.sum(filtered[filtered.size//2:])) / np.sum(filtered)
    # Return preprocessed data
    return {'mean': mean, 'std': std, 'max_val': max_val, 'min_val': min_val, 'distribution': distribution, 'symmetry': symmetry}
