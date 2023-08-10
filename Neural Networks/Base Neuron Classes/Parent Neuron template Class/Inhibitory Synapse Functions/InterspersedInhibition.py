import numpy as np

class InterspersedInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, interspersed_neurons=None, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

        if interspersed_neurons is None:
            self.interspersed_neurons = np.random.randint(0, self.num_neurons, self.num_neurons // 2)
        else:
            self.interspersed_neurons = interspersed_neurons

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_interspersed_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in self.interspersed_neurons:
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply the interspersed inhibition effect
        activity_levels -= np.sum(total_inhibition, axis=1) * self.inhibitory_strength

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

