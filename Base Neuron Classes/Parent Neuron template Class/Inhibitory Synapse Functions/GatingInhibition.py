import numpy as np

class GatingInhibition:
    def __init__(self, num_neurons, num_gates, initial_connectivity=None, gating_threshold=0.5, inhibitory_strength=0.5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.num_gates = num_gates
        self.gating_threshold = gating_threshold
        self.inhibitory_strength = inhibitory_strength

        if initial_connectivity is None:
            self.connectivity_gate_neuron = np.random.uniform(min_strength, max_strength, (self.num_gates, self.num_neurons))
        else:
            self.connectivity_gate_neuron = initial_connectivity

    def compute_gating(self, activity_levels):
        gating = np.dot(activity_levels, self.connectivity_gate_neuron.T)
        gating = np.where(gating > self.gating_threshold, 1, 0)
        return gating

    def apply_gating_inhibition(self, activity_levels):
        # Calculate the gating effect based on the activity levels
        gating_effect = self.compute_gating(activity_levels)

        # Calculate the gating inhibition for each neuron
        gating_inhibition = np.dot(gating_effect, self.connectivity_gate_neuron)

        # Apply the gating inhibition to the activity levels
        activity_levels -= gating_inhibition * self.inhibitory_strength

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

