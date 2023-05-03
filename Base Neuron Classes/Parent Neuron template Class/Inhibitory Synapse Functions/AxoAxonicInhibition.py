import numpy as np

class AxoAxonicInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, axon_strength=0.3, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.axon_strength = axon_strength
        
        if initial_connectivity is None:
            self.inhibitory_connectivity_axon = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.inhibitory_connectivity_axon = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.inhibitory_connectivity_axon
        return inhibition

    def apply_axo_axonic_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply the overall axo-axonic inhibition effect
        axon_inhibition_effect = np.dot(total_inhibition, activity_levels) * self.axon_strength

        # Modify the activity levels based on the axo-axonic inhibition
        activity_levels -= axon_inhibition_effect

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

