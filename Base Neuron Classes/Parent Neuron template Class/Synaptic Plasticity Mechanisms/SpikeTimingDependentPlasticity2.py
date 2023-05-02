import numpy as np

class SpikeTimingDependentPlasticity2:
    def __init__(self, potentiation_rate, depression_rate, time_window, activation_function):
        self.potentiation_rate = potentiation_rate
        self.depression_rate = depression_rate
        self.time_window = time_window
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

    def update_synapses(self, synapse_strengths, pre_synaptic_activity, post_synaptic_activity):
        delta_t = pre_synaptic_activity - post_synaptic_activity
        if np.abs(delta_t) <= self.time_window:
            if delta_t > 0:
                synapse_strengths *= (1 + self.potentiation_rate)
            else:
                synapse_strengths *= (1 - self.depression_rate)
        synapse_strengths = np.clip(synapse_strengths, 0, 1)
        return synapse_strengths

