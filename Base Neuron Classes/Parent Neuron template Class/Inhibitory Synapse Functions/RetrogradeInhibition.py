import numpy as np

class RetrogradeInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, retrograde_strength=0.3, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.retrograde_strength = retrograde_strength

        if initial_connectivity is None:
            self.retrograde_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.retrograde_connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(post_synaptic_activity, pre_synaptic_activity)  # Note the order of post and pre-synaptic activity
        inhibition *= self.retrograde_connectivity
        return inhibition

    def apply_retrograde_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply the overall retrograde inhibition effect
        retrograde_inhibition_effect = np.dot(total_inhibition, activity_levels) * self.retrograde_strength

        # Modify the activity levels based on the retrograde inhibition
        activity_levels -= retrograde_inhibition_effect

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels


