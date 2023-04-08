import numpy as np
import skimage.feature

def preprocess_texture_data(data):
    # Normalize data to [0, 1] range
    data = (data - np.min(data)) / (np.max(data) - np.min(data))
    # Calculate texture features such as contrast, energy, and homogeneity
    glcm = skimage.feature.greycomatrix(data, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)
    contrast = skimage.feature.greycoprops(glcm, 'contrast').mean()
    energy = skimage.feature.greycoprops(glcm, 'energy').mean()
    homogeneity = skimage.feature.greycoprops(glcm, 'homogeneity').mean()
    correlation = skimage.feature.greycoprops(glcm, 'correlation').mean()
    # Return preprocessed data
    return {'contrast': contrast, 'energy': energy, 'homogeneity': homogeneity, 'correlation': correlation}
