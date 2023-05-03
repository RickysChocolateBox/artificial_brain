import numpy as np

class InhibitionStabilizedSparsification:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, sparsification_threshold=0.3, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.sparsification_threshold = sparsification_threshold

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_sparsification(self, activity_levels):
        sparsified_activity = np.where(activity_levels < self.sparsification_threshold, 0, activity_levels)
        return sparsified_activity

    def apply_inhibition_stabilized_sparsification(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply inhibition-stabilized sparsification
        sparsified_activity = self.apply_sparsification(activity_levels)

        # Modify the activity levels based on the inhibition and sparsification
        activity_levels -= np.dot(total_inhibition, sparsified_activity)

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

