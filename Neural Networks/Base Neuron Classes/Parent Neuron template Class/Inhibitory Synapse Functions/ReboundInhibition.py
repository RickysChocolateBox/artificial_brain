import numpy as np

class ReboundInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, min_strength=-1, max_strength=0, rebound_threshold=0.5):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.rebound_threshold = rebound_threshold
        
        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_rebound_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    total_inhibition[i, j] = inhibition

        # Apply the rebound inhibition effect
        rebound_inhibition = np.where(activity_levels < self.rebound_threshold,
                                      np.sum(total_inhibition, axis=0) * self.inhibitory_strength,
                                      0)

        # Modify the activity levels based on the rebound inhibition
        activity_levels -= rebound_inhibition

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

