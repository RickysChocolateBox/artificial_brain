import numpy as np

class IncreaseInNeurotransmitterRelease:
    def __init__(self, release_rate, learning_rate, activation_function, threshold):
        self.release_rate = release_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.threshold = threshold

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_release_level(self, release_level, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_release_level = self.release_rate * activity_level
        release_level += self.learning_rate * change_in_release_level
        release_level = np.clip(release_level, -self.threshold, self.threshold)
        return release_level

