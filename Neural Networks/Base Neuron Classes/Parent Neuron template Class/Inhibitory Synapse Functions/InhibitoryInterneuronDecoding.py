import numpy as np

class InhibitoryInterneuronDecoding:
    def __init__(self, num_neurons, num_patterns, initial_connectivity=None, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.num_patterns = num_patterns

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_patterns, self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity, pattern_idx):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity[pattern_idx]
        return inhibition

    def apply_decoding(self, activity_levels, pattern_idx):
        new_activity_levels = np.zeros_like(activity_levels)

        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity, pattern_idx)
                    new_activity_levels[j] += inhibition

        new_activity_levels = np.clip(new_activity_levels, 0, 1)

        return new_activity_levels

