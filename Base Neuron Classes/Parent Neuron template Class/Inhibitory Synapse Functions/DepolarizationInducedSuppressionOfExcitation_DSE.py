import numpy as np

class DepolarizationInducedSuppressionOfExcitation_DSE:
    def __init__(self, num_neurons, initial_connectivity=None, excitatory_strength=0.5, depolarization_threshold=0.7, suppression_factor=0.5, min_strength=0, max_strength=1):
        self.num_neurons = num_neurons
        self.excitatory_strength = excitatory_strength
        self.depolarization_threshold = depolarization_threshold
        self.suppression_factor = suppression_factor

        if initial_connectivity is None:
            self.dse_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.dse_connectivity = initial_connectivity

    def compute_excitation(self, pre_synaptic_activity, post_synaptic_activity):
        excitation = np.outer(pre_synaptic_activity, post_synaptic_activity)
        excitation *= self.dse_connectivity
        return excitation

    def suppress_excitation(self, activity_levels):
        suppressed = np.where(activity_levels > self.depolarization_threshold, self.suppression_factor * activity_levels, activity_levels)
        return suppressed

    def apply_dse(self, activity_levels):
        # Calculate the total excitation for each neuron pair
        total_excitation = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_excitation[i, j] = self.compute_excitation(pre_synaptic_activity, post_synaptic_activity)

        # Apply depolarization-induced suppression of excitation
        suppressed_activity = self.suppress_excitation(activity_levels)

        # Modify the activity levels based on DSE
        activity_levels -= total_excitation * suppressed_activity[:, np.newaxis]

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

