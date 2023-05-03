import numpy as np

class DelayedInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, min_strength=-1, max_strength=0, delay=1):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.delay = delay
        
        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

        self.activity_buffer = np.zeros((self.delay + 1, self.num_neurons))

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_delayed_inhibition(self, activity_levels):
        # Shift the activity buffer to add the current activity levels
        self.activity_buffer[:-1] = self.activity_buffer[1:]
        self.activity_buffer[-1] = activity_levels

        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = self.activity_buffer[-(self.delay + 1), i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    total_inhibition[i, j] = inhibition

        # Apply the delayed inhibition effect
        delayed_inhibition = np.sum(total_inhibition, axis=0) * self.inhibitory_strength

        # Modify the activity levels based on the delayed inhibition
        activity_levels -= delayed_inhibition

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

