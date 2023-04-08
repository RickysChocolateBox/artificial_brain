import numpy as np

def preprocess_motor_position_data(data):
    # Calculate statistics such as mean and variance
    mean = np.mean(data)
    std = np.std(data)
    max_val = np.max(data)
    min_val = np.min(data)
    # Detect changes and calculate their properties
    diff = np.diff(data)
    changes = np.where(diff != 0)[0] + 1
    properties = np.zeros((changes.size, 2))
    properties[:, 0] = np.diff(np.concatenate((np.array([0]), changes)))
    properties[:, 1] = np.diff(data[changes-1])
    # Calculate additional features
    mean_change = np.mean(properties[:, 1])
    std_change = np.std(properties[:, 1])
    max_change = np.max(properties[:, 1])
    min_change = np.min(properties[:, 1])
    # Return preprocessed data
    return {'mean': mean, 'std': std, 'max_val': max_val, 'min_val': min_val, 'changes': changes, 'properties': properties, 'mean_change': mean_change, 'std_change': std_change, 'max_change': max_change, 'min_change': min_change}
