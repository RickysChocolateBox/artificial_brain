import numpy as np

class LateralInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, lateral_strength=0.3, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.lateral_strength = lateral_strength
        
        if initial_connectivity is None:
            self.lateral_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.lateral_connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.lateral_connectivity
        return inhibition

    def apply_lateral_inhibition(self, activity_levels):
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        lateral_inhibition_effect = np.dot(total_inhibition, activity_levels) * self.lateral_strength
        activity_levels -= lateral_inhibition_effect
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels
