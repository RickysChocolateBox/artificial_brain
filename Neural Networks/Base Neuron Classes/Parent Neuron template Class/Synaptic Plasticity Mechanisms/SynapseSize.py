import numpy as np

class SynapseSize:
    def __init__(self, initial_size, learning_rate, activation_function='sigmoid', noise_factor=0.1):
        self.synapse_size = initial_size
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.noise_factor = noise_factor

    def sigmoid(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        # ReLU activation function
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        # Apply the chosen activation function
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_synapse_size(self, activity_levels):
        # Add random noise to activity levels
        noise = np.random.normal(0, self.noise_factor, len(activity_levels))
        activity_levels += noise

        # Apply the activation function to the activity levels
        regulated_levels = self.apply_activation_function(activity_levels)

        # Calculate the change in synapse size
        delta_size = self.learning_rate * regulated_levels

        # Update the synapse size
        self.synapse_size += delta_size
        self.synapse_size = np.clip(self.synapse_size, 0, 1)

        return self.synapse_size

