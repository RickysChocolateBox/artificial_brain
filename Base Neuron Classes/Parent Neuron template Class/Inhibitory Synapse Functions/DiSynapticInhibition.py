import numpy as np

class DiSynapticInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_di_synaptic_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    total_inhibition[i, j] = inhibition

        # Find the second-largest inhibition for each neuron and apply the di-synaptic inhibition effect
        di_synaptic_inhibition = np.partition(total_inhibition, -2, axis=1)[:, -2] * self.inhibitory_strength

        # Modify the activity levels based on the di-synaptic inhibition
        activity_levels -= di_synaptic_inhibition

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

