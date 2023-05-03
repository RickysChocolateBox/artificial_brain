import numpy as np

class FastInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, fast_strength=0.3, min_strength=-1, max_strength=0, fast_time_constant=0.1):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.fast_strength = fast_strength
        self.fast_time_constant = fast_time_constant

        if initial_connectivity is None:
            self.fast_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.fast_connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.fast_connectivity
        return inhibition

    def apply_fast_inhibition(self, activity_levels, dt):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply the overall fast inhibition effect
        fast_inhibition_effect = np.dot(total_inhibition, activity_levels) * self.fast_strength

        # Modify the activity levels based on the fast inhibition
        activity_levels -= fast_inhibition_effect * dt / self.fast_time_constant

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

