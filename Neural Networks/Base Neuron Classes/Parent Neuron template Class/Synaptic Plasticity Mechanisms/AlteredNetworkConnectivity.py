import numpy as np

class AlteredNetworkConnectivity:
    def __init__(self, learning_rate, connectivity_change_rate, noise_std_dev):
        self.learning_rate = learning_rate
        self.connectivity_change_rate = connectivity_change_rate
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update connectivity strength based on activity level and noise
    def update_connectivity_strength(self, connectivity_strength, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update connectivity strength based on activity level
        connectivity_strength += self.learning_rate * self.connectivity_change_rate * activity_level

        return connectivity_strength

