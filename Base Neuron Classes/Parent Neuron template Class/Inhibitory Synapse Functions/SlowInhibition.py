import numpy as np

class SlowInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, slow_strength=0.3, min_strength=-1, max_strength=0, slow_time_constant=1.0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.slow_strength = slow_strength
        self.slow_time_constant = slow_time_constant

        if initial_connectivity is None:
            self.slow_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.slow_connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.slow_connectivity
        return inhibition

    def apply_slow_inhibition(self, activity_levels, dt):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply the overall slow inhibition effect
        slow_inhibition_effect = np.dot(total_inhibition, activity_levels) * self.slow_strength

        # Modify the activity levels based on the slow inhibition
        activity_levels -= slow_inhibition_effect * dt / self.slow_time_constant

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

