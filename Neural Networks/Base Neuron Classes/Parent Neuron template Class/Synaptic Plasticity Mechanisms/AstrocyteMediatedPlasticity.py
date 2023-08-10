import numpy as np

class AstrocyteMediatedPlasticity:
    def __init__(self, astrocyte_influence_rate, activation_function):
        self.astrocyte_influence_rate = astrocyte_influence_rate
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

    def astrocyte_influence(self, synapse_strengths, astrocyte_activity):
        astrocyte_activity = self.apply_activation_function(astrocyte_activity)
        synapse_strengths *= (1 + self.astrocyte_influence_rate * astrocyte_activity)
        synapse_strengths = np.clip(synapse_strengths, 0, 1)
        return synapse_strengths
