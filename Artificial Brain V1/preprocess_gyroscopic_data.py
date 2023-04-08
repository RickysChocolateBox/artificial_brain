import numpy as np

def preprocess_gyroscopic_data(data):
    # Calculate statistics such as mean and variance
    stats = {}
    for axis in range(3):
        axis_data = data[:, axis]
        stats[f"mean_{axis}"] = np.mean(axis_data)
        stats[f"std_{axis}"] = np.std(axis_data)
        stats[f"max_{axis}"] = np.max(axis_data)
        stats[f"min_{axis}"] = np.min(axis_data)
    # Return preprocessed data
    return stats
