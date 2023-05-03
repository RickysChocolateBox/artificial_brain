import numpy as np

class FeedforwardInhibition:
    def __init__(self, num_neurons, feedforward_factors=None, feedforward_matrix=None, modulation_factors=None, time_constant=1.0):
        self.num_neurons = num_neurons
        # Initialize feedforward factors, connections, and modulation factors
        if feedforward_factors is None:
            self.feedforward_factors = np.ones(num_neurons)
        else:
            self.feedforward_factors = feedforward_factors

        if feedforward_matrix is None:
            self.feedforward_matrix = np.eye(num_neurons)
        else:
            self.feedforward_matrix = feedforward_matrix

        if modulation_factors is None:
            self.modulation_factors = np.ones(num_neurons)
        else:
            self.modulation_factors = modulation_factors
        
        self.time_constant = time_constant
        self.feedforward_activity = np.zeros(num_neurons)

    def update_feedforward_activity(self, neuron_inputs, modulatory_inputs):
        # Calculate feedforward activity based on neuron inputs, connections, and modulatory inputs
        feedforward_activity_new = np.dot(self.feedforward_matrix, neuron_inputs) * self.modulation_factors * modulatory_inputs
        self.feedforward_activity += (-self.feedforward_activity + feedforward_activity_new) / self.time_constant

    def apply_inhibition(self, neuron_inputs):
        # Apply feedforward inhibition to neuron inputs
        return neuron_inputs - self.feedforward_factors * self.feedforward_activity

