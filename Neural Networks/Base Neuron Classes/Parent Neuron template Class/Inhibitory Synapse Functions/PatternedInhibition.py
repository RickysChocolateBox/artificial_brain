import numpy as np

class PatternedInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, pattern=None, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength

        if initial_connectivity is None:
            self.patterned_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.patterned_connectivity = initial_connectivity

        if pattern is None:
            self.pattern = np.random.uniform(0, 1, self.num_neurons)
        else:
            self.pattern = pattern

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.patterned_connectivity
        return inhibition

    def apply_patterned_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply pattern to inhibition
        patterned_inhibition = total_inhibition * self.pattern[:, np.newaxis]

        # Modify the activity levels based on patterned inhibition
        activity_levels -= patterned_inhibition

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

