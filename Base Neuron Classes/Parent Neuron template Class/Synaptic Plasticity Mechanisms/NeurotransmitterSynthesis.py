import numpy as np

class NeurotransmitterSynthesis:
    def __init__(self, synthesis_rate, activation_function='sigmoid'):
        self.synthesis_rate = synthesis_rate
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

    def update_synthesis(self, neurotransmitter_amount, activity_levels):
        activity_levels = self.apply_activation_function(activity_levels)
        neurotransmitter_synthesis = self.synthesis_rate * activity_levels
        neurotransmitter_amount += neurotransmitter_synthesis
        return neurotransmitter_amount

