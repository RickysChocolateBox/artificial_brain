import numpy as np

class DendriticSpineMotilityChanges:
    def __init__(self, motility_rate, learning_rate, activation_function, threshold):
        self.motility_rate = motility_rate
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

    def update_spine_motility(self, spine_motility, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_motility = self.motility_rate * activity_level
        spine_motility += self.learning_rate * change_in_motility
        spine_motility = np.clip(spine_motility, -self.threshold, self.threshold)
        return spine_motility

