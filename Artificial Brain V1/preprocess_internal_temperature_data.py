import numpy as np
import scipy.signal as signal

def preprocess_internal_temperature_data(data):
    # Apply high-pass filter to remove baseline drift
    sos = signal.butter(4, 0.01, btype='highpass', fs=data['sampling_rate'], output='sos')
    filtered = signal.sosfilt(sos, data['temperature'])
    # Calculate temperature statistics such as mean and variance
    mean = np.mean(filtered)
    std = np.std(filtered)
    max_val = np.max(filtered)
    min_val = np.min(filtered)
    # Detect peaks and calculate their properties
    peaks, _ = signal.find_peaks(filtered, distance=100, prominence=0.1)
    properties = signal.peak_widths(filtered, peaks, rel_height=0.5)
    peak_widths = properties[0]
    peak_heights = properties[1]
    # Return preprocessed data
    return {'mean': mean, 'std': std, 'max_val': max_val, 'min_val': min_val, 'peak_widths': peak_widths, 'peak_heights': peak_heights}
