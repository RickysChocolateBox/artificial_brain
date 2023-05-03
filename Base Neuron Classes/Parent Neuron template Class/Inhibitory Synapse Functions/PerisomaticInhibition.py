import numpy as np

class PerisomaticInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, perisomatic_strength=0.3, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.perisomatic_strength = perisomatic_strength
        
        if initial_connectivity is None:
            self.perisomatic_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.perisomatic_connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.perisomatic_connectivity
        return inhibition

    def apply_perisomatic_inhibition(self, activity_levels):
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        perisomatic_inhibition_effect = np.dot(total_inhibition, activity_levels) * self.perisomatic_strength
        activity_levels -= perisomatic_inhibition_effect
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

