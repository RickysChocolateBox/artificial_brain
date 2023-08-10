import numpy as np

class SynapticConsolidation:
    def __init__(self, consolidation_rate, decay_factor, learning_rate, activation_function='sigmoid'):
        self.consolidation_rate = consolidation_rate
        self.decay_factor = decay_factor
        self.learning_rate = learning_rate
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

    def update_synaptic_weights(self, synaptic_weights, activity_levels):
        # Apply the activation function to activity levels
        activity_levels = self.apply_activation_function(activity_levels)

        # Calculate weight updates based on activity levels and consolidation rate
        weight_updates = self.learning_rate * self.consolidation_rate * activity_levels

        # Update the synaptic weights
        synaptic_weights += weight_updates

        # Decay the synaptic weights
        synaptic_weights *= (1 - self.decay_factor)

        return synaptic_weights

