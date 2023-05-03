import numpy as np

class InhibitoryInterneuronLanguageProcessing:
    def __init__(self, num_neurons, inhibition_strength=0.5, language_threshold=0.6, learning_rate=0.01, plasticity_rate=0.1):
        self.num_neurons = num_neurons
        self.inhibition_strength = inhibition_strength
        self.language_threshold = language_threshold
        self.learning_rate = learning_rate
        self.plasticity_rate = plasticity_rate
        self.connectivity_matrix = np.random.uniform(0, inhibition_strength, (num_neurons, num_neurons))
        np.fill_diagonal(self.connectivity_matrix, 0)
        self.language_weights = np.random.uniform(0, 1, num_neurons)
        self.language_trace = np.zeros(num_neurons)

    def compute_inhibition(self, pre_activity, post_activity):
        inhibition = np.dot(pre_activity, self.connectivity_matrix * post_activity[:, None])
        return inhibition

    def update_weights(self, activity_levels):
        self.connectivity_matrix += self.learning_rate * np.outer(activity_levels, activity_levels)
        np.fill_diagonal(self.connectivity_matrix, 0)
        self.connectivity_matrix.clip(min=0, max=self.inhibition_strength, out=self.connectivity_matrix)

    def update_language_weights(self, activity_levels):
        self.language_trace = self.plasticity_rate * activity_levels + (1 - self.plasticity_rate) * self.language_trace
        self.language_weights += self.learning_rate * (activity_levels - self.language_weights) * self.language_trace

    def update_activity(self, activity_levels):
        high_activity_neurons = activity_levels >= self.language_threshold
        inhibition = self.compute_inhibition(activity_levels, high_activity_neurons)
        activity_levels -= inhibition
        activity_levels.clip(min=0, max=1, out=activity_levels)
        self.update_weights(activity_levels)
        self.update_language_weights(activity_levels)
        return activity_levels

    def language_neurons(self, activity_levels):
        return np.argwhere(activity_levels >= self.language_threshold).flatten()


