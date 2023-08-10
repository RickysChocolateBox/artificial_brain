import numpy as np

class InhibitoryInterneuronDecisionMaking:
    def __init__(self, num_neurons, inhibition_strength=0.5, learning_rate=0.01, decision_threshold=0.8):
        self.num_neurons = num_neurons
        self.inhibition_strength = inhibition_strength
        self.learning_rate = learning_rate
        self.decision_threshold = decision_threshold
        self.connectivity_matrix = np.random.uniform(0, inhibition_strength, (num_neurons, num_neurons))
        np.fill_diagonal(self.connectivity_matrix, 0)

    def compute_inhibition(self, pre_activity, post_activity):
        inhibition = np.dot(pre_activity, self.connectivity_matrix * post_activity[:, None])
        return inhibition

    def update_weights(self, activity_levels):
        self.connectivity_matrix += self.learning_rate * np.outer(activity_levels, activity_levels)
        np.fill_diagonal(self.connectivity_matrix, 0)
        self.connectivity_matrix.clip(min=0, max=self.inhibition_strength, out=self.connectivity_matrix)

    def update_activity(self, activity_levels):
        high_activity_neurons = activity_levels >= self.decision_threshold
        inhibition = self.compute_inhibition(activity_levels, high_activity_neurons)
        activity_levels -= inhibition
        activity_levels.clip(min=0, max=1, out=activity_levels)
        self.update_weights(activity_levels)
        return activity_levels

    def make_decision(self, activity_levels):
        decision_index = np.argmax(activity_levels)
        return decision_index

