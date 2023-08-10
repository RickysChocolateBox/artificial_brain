import numpy as np

class SynapseShape:
    def __init__(self, initial_shape, learning_rate, shape_function='sigmoid', noise_factor=0.1):
        self.synapse_shape = initial_shape
        self.learning_rate = learning_rate
        self.shape_function = shape_function
        self.noise_factor = noise_factor

    def sigmoid(self, x):
        # Sigmoid function
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        # ReLU function
        return np.maximum(0, x)

    def apply_shape_function(self, x):
        # Apply the chosen shape function
        if self.shape_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.shape_function == 'relu':
            return self.relu(x)

    def update_synapse_shape(self, activity_levels):
        # Add random noise to activity levels
        noise = np.random.normal(0, self.noise_factor, len(activity_levels))
        activity_levels += noise

        # Apply the shape function to the activity levels
        regulated_levels = self.apply_shape_function(activity_levels)

        # Calculate the change in synapse shape
        delta_shape = self.learning_rate * regulated_levels

        # Update the synapse shape
        self.synapse_shape += delta_shape
        self.synapse_shape = np.clip(self.synapse_shape, 0, 1)

        return self.synapse_shape

