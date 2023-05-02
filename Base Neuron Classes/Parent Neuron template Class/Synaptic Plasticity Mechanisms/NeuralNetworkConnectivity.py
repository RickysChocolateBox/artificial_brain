import numpy as np

class NeuralNetworkConnectivity:
    def __init__(self, connectivity_rate, threshold, activation_function='sigmoid'):
        self.connectivity_rate = connectivity_rate
        self.threshold = threshold
        self.activation_function = activation_function

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_connectivity(self, connectivity_matrix, activity_levels):
        # Apply the specified activation function to the activity levels
        activity_levels = self.apply_activation_function(activity_levels)

        # Calculate connectivity change based on the connectivity rate and activity levels
        connectivity_change = self.connectivity_rate * np.outer(activity_levels, activity_levels)

        # Update the connectivity matrix and clip values to maintain stability
        connectivity_matrix += connectivity_change
        connectivity_matrix = np.clip(connectivity_matrix, -self.threshold, self.threshold)

        return connectivity_matrix

