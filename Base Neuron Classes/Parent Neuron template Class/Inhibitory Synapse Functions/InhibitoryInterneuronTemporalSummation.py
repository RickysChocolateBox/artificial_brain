import numpy as np

class InhibitoryInterneuronTemporalSummation:
    def __init__(self, num_neurons, initial_connectivity=None, time_constant=5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.time_constant = time_constant

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

        self.previous_inhibition = np.zeros((self.num_neurons, self.num_neurons))

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_temporal_summation(self, activity_levels):
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))

        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    total_inhibition[i, j] = inhibition

        decayed_previous_inhibition = self.previous_inhibition * np.exp(-1 / self.time_constant)
        updated_inhibition = total_inhibition + decayed_previous_inhibition
        self.previous_inhibition = updated_inhibition

        activity_levels = np.clip(activity_levels - np.sum(updated_inhibition, axis=0), 0, 1)

        return activity_levels

