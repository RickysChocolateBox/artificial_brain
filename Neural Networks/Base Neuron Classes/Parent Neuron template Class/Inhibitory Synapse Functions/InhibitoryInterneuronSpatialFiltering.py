import numpy as np

class InhibitoryInterneuronSpatialFiltering:
    def __init__(self, num_neurons, initial_connectivity=None, spatial_filtering_strength=0.5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.spatial_filtering_strength = spatial_filtering_strength

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_spatial_filtering(self, activity_levels):
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))

        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    total_inhibition[i, j] = inhibition

        spatial_filtering = np.sum(total_inhibition, axis=0) * self.spatial_filtering_strength
        activity_levels -= spatial_filtering

        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

