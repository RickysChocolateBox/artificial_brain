import numpy as np

class NeurotransmitterReleaseProbability2:
    def __init__(self, release_rate, activation_function='sigmoid'):
        self.release_rate = release_rate
        self.activation_function = activation_function

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_release_probability(self, release_probabilities, activity_levels):
        activity_levels = self.apply_activation_function(activity_levels)
        release_probability_change = self.release_rate * activity_levels
        release_probabilities += release_probability_change
        release_probabilities = np.clip(release_probabilities, 0, 1)
        return release_probabilities

