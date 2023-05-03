import numpy as np

class InhibitoryInterneuronCompetition:
    def __init__(self, num_neurons, initial_connectivity=None, competition_rate=0.1, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.competition_rate = competition_rate
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

    def update_competition(self, activity_levels, min_strength, max_strength):
        max_activity = np.max(activity_levels)
        self.connectivity += self.competition_rate * (max_activity - activity_levels)
        self.connectivity = np.clip(self.connectivity, min_strength, max_strength)

    def apply_competition(self, activity_levels):
        self.update_competition(activity_levels, self.min_strength, self.max_strength)

        new_activity_levels = np.zeros_like(activity_levels)

        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    inhibition = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)
                    new_activity_levels[j] -= inhibition

        new_activity_levels = np.clip(new_activity_levels, 0, 1)

        return new_activity_levels


