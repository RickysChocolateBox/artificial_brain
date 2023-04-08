import numpy as np
import scipy.signal as signal
import librosa
from sklearn.preprocessing import StandardScaler

def preprocess_stereo_hearing_data(data):
    # Apply bandpass filter to remove noise and enhance speech signal
    b, a = signal.butter(4, [300, 3400], btype='bandpass', fs=data['sampling_rate'])
    filtered_left = signal.filtfilt(b, a, data['left'])
    filtered_right = signal.filtfilt(b, a, data['right'])
    # Perform feature extraction and pattern recognition
    mfcc_left = librosa.feature.mfcc(y=filtered_left, sr=data['sampling_rate'], n_mfcc=20)
    mfcc_right = librosa.feature.mfcc(y=filtered_right, sr=data['sampling_rate'], n_mfcc=20)
    delta_mfcc_left = librosa.feature.delta(mfcc_left, order=1)
    delta_mfcc_right = librosa.feature.delta(mfcc_right, order=1)
    features_left = np.vstack((mfcc_left, delta_mfcc_left))
    features_right = np.vstack((mfcc_right, delta_mfcc_right))
    # Apply standardization to the features
    scaler = StandardScaler()
    scaler.fit(np.hstack((features_left, features_right)))
    features_left = scaler.transform(features_left)
    features_right = scaler.transform(features_right)
    # Compute cosine similarity between the left and right features
    cosine_dist = np.dot(features_left.ravel(), features_right.ravel()) / (np.linalg.norm(features_left.ravel()) * np.linalg.norm(features_right.ravel()))
    # Calculate additional statistics such as mean and variance of MFCCs
    mfcc_mean_left = np.mean(mfcc_left)
    mfcc_std_left = np.std(mfcc_left)
    mfcc_mean_right = np.mean(mfcc_right)
    mfcc_std_right = np.std(mfcc_right)
    # Return preprocessed data
    return {'mfcc_left': mfcc_left, 'mfcc_right': mfcc_right, 'delta_mfcc_left': delta_mfcc_left, 'delta_mfcc_right': delta_mfcc_right, 'cosine_dist': cosine_dist, 'mfcc_mean_left': mfcc_mean_left, 'mfcc_std_left': mfcc_std_left, 'mfcc_mean_right': mfcc_mean_right, 'mfcc_std_right': mfcc_std_right}
