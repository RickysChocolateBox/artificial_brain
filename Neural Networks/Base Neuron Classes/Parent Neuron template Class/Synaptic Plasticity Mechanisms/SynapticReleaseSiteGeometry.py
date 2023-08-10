import numpy as np

class SynapticReleaseSiteGeometry:
    def __init__(self, geometry_modulation_rate, modulation_threshold, noise_std_dev):
        self.geometry_modulation_rate = geometry_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update synaptic release site geometry based on activity level and noise
    def update_geometry(self, geometry_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update geometry state based on activity level
        if activity_level >= self.modulation_threshold:
            geometry_state += self.geometry_modulation_rate
        else:
            geometry_state -= self.geometry_modulation_rate

        return geometry_state

