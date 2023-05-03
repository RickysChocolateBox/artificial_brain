import numpy as np

class InhibitoryInterneuronNoiseReduction:
    def __init__(self, num_neurons, initial_connectivity=None, noise_reduction_factor=0.5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.noise_reduction_factor = noise_reduction_factor

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_noise_reduction(self, activity_levels):
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    total_inhibition[i, j] = inhibition

        noise_reduction = np.sum(total_inhibition, axis=0) * self.noise_reduction_factor
        activity_levels -= noise_reduction

        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

