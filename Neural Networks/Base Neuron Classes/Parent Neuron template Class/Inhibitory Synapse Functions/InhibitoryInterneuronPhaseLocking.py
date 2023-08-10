import numpy as np

class InhibitoryInterneuronPhaseLocking:
    def __init__(self, num_neurons, initial_connectivity=None, min_strength=-1, max_strength=0, phase_lock_threshold=0.5):
        self.num_neurons = num_neurons
        self.phase_lock_threshold = phase_lock_threshold

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def apply_phase_locking(self, activity_levels):
        phase_locked_neurons = []

        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

                    if np.abs(inhibition) > self.phase_lock_threshold:
                        phase_locked_neurons.append((i, j))

        for (i, j) in phase_locked_neurons:
            activity_levels[j] = activity_levels[i]

        return activity_levels
