import numpy as np

class ChangesInNeurotransmitterStorage:
    def __init__(self, storage_capacity, storage_rate, release_rate, activation_function='sigmoid', noise_factor=0.1):
        self.storage_capacity = storage_capacity
        self.storage_rate = storage_rate
        self.release_rate = release_rate
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

    def update_storage(self, neurotransmitter_levels):
        # Add random noise to neurotransmitter levels
        noise = np.random.normal(0, self.noise_factor, len(neurotransmitter_levels))
        neurotransmitter_levels += noise

        # Apply the activation function to the neurotransmitter levels
        regulated_levels = self.apply_activation_function(neurotransmitter_levels)

        # Calculate the change in storage
        delta_storage = self.storage_rate * regulated_levels

        # Update neurotransmitter storage based on storage capacity
        neurotransmitter_storage = np.clip(delta_storage, 0, self.storage_capacity)

        # Release neurotransmitters based on the release rate
        neurotransmitter_release = self.release_rate * neurotransmitter_storage

        return neurotransmitter_release, neurotransmitter_storage

