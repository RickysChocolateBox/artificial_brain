import numpy as np

class InhibitorySurround:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, surround_radius=1, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.surround_radius = surround_radius

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_inhibitory_surround(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if abs(i - j) <= self.surround_radius and i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply the inhibitory surround effect
        activity_levels -= np.sum(total_inhibition, axis=1) * self.inhibitory_strength

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

