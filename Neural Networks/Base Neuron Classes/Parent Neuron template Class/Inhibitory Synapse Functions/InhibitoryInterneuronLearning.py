import numpy as np

class InhibitoryInterneuronLearning:
    def __init__(self, num_neurons, initial_connectivity=None, learning_rate=0.1, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.learning_rate = learning_rate
        self.min_strength = min_strength
        self.max_strength = max_strength

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def update_learning(self, pre_synaptic_activity, post_synaptic_activity, min_strength, max_strength):
        self.connectivity += self.learning_rate * np.outer(pre_synaptic_activity, post_synaptic_activity)
        self.connectivity = np.clip(self.connectivity, min_strength, max_strength)

    def apply_learning(self, activity_levels):
        new_activity_levels = np.zeros_like(activity_levels)

        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    new_activity_levels[j] -= inhibition

        new_activity_levels = np.clip(new_activity_levels, 0, 1)
        self.update_learning(activity_levels, new_activity_levels, self.min_strength, self.max_strength)

        return new_activity_levels

