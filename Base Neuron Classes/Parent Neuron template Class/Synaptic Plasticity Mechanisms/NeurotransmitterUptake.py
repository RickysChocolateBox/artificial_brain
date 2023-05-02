import numpy as np

class NeurotransmitterUptake:
    def __init__(self, uptake_rate, activation_function='sigmoid'):
        self.uptake_rate = uptake_rate
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

    def update_uptake(self, neurotransmitter_amount, activity_levels):
        activity_levels = self.apply_activation_function(activity_levels)
        neurotransmitter_uptake = self.uptake_rate * activity_levels
        neurotransmitter_amount -= neurotransmitter_uptake
        neurotransmitter_amount = np.maximum(0, neurotransmitter_amount)
        return neurotransmitter_amount

