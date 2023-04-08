import numpy as np
import scipy.signal as signal
from sklearn.cluster import DBSCAN

def preprocess_lidar_data(data):
    # Apply median filter to remove noise
    filtered = signal.medfilt(data, kernel_size=3)
    # Convert polar coordinates to cartesian coordinates
    ranges = np.arange(data.size) * data['range_resolution'] + data['range_offset']
    angles = np.linspace(data['angle_min'], data['angle_max'], data.size)
    x = filtered * np.sin(angles)
    y = filtered * np.cos(angles)
    # Perform clustering to identify objects
    points = np.stack((x, y), axis=-1)
    dbscan = DBSCAN(eps=0.1, min_samples=10)
    clusters = dbscan.fit_predict(points)
    unique_clusters = np.unique(clusters)
    # Calculate features for each cluster such as position and size
    positions = []
    sizes = []
    for cluster_id in unique_clusters:
        if cluster_id == -1:
            continue
        cluster_points = points[clusters == cluster_id]
        x_mean = np.mean(cluster_points[:, 0])
        y_mean = np.mean(cluster_points[:, 1])
        size = cluster_points.shape[0]
        positions.append({'x_mean': x_mean, 'y_mean': y_mean})
        sizes.append(size)
    # Calculate statistics such as mean and variance of the sizes
    sizes_mean = np.mean(sizes)
    sizes_std = np.std(sizes)
    sizes_max = np.max(sizes)
    sizes_min = np.min(sizes)
    # Return preprocessed data
    return {'positions': positions, 'sizes_mean': sizes_mean, 'sizes_std': sizes_std, 'sizes_max': sizes_max, 'sizes_min': sizes_min}
