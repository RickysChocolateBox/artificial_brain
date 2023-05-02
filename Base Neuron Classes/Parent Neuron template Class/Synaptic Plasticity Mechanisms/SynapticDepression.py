import numpy as np

class SynapticDepression:
    def __init__(self, depression_rate, threshold, activation_function):
        self.depression_rate = depression_rate
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

    def depress_synapses(self, synapse_strengths, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        depression_factor = self.depression_rate * activity_level
        synapse_strengths *= (1 - depression_factor)
        synapse_strengths = np.clip(synapse_strengths, 0, self.threshold)
        return synapse_strengths

