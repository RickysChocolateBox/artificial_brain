import numpy as np

class SpatiallyTunedInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, spatial_tuning=0.5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.spatial_tuning = spatial_tuning

        if initial_connectivity is None:
            self.spatial_tuned_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.spatial_tuned_connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.spatial_tuned_connectivity
        return inhibition

    def apply_spatial_tuning(self, inhibition):
        tuned_inhibition = inhibition * self.spatial_tuning
        return tuned_inhibition

    def apply_spatially_tuned_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply spatial tuning
        total_inhibition = self.apply_spatial_tuning(total_inhibition)

        # Modify the activity levels based on spatially tuned inhibition
        activity_levels -= total_inhibition

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

