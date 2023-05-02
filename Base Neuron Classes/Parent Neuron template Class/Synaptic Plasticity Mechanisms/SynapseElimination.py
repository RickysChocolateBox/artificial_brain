import numpy as np

class SynapseElimination:
    def __init__(self, elimination_rate, threshold, activation_function):
        self.elimination_rate = elimination_rate
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

    def eliminate_synapses(self, synapse_strengths, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        elimination_factor = self.elimination_rate * activity_level
        synapse_strengths -= elimination_factor
        synapse_strengths = np.clip(synapse_strengths, 0, self.threshold)
        return synapse_strengths

