import numpy as np

class DepolarizationInducedSuppressionOfInhibition_DSI:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, depolarization_threshold=0.7, suppression_factor=0.5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.depolarization_threshold = depolarization_threshold
        self.suppression_factor = suppression_factor

        if initial_connectivity is None:
            self.dsi_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.dsi_connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.dsi_connectivity
        return inhibition

    def suppress_inhibition(self, activity_levels):
        suppressed = np.where(activity_levels > self.depolarization_threshold, self.suppression_factor * activity_levels, activity_levels)
        return suppressed

    def apply_dsi(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply depolarization-induced suppression of inhibition
        suppressed_activity = self.suppress_inhibition(activity_levels)

        # Modify the activity levels based on DSI
        activity_levels -= total_inhibition * suppressed_activity[:, np.newaxis]

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

