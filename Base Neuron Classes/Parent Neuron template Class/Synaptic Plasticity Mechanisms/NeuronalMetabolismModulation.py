import numpy as np

class NeuronalMetabolismModulation:
    def __init__(self, metabolism_rate, learning_rate, activation_function, threshold):
        self.metabolism_rate = metabolism_rate
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

    def update_metabolism(self, metabolism_activity, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_metabolism_activity = self.metabolism_rate * activity_level
        metabolism_activity += self.learning_rate * change_in_metabolism_activity
        metabolism_activity = np.clip(metabolism_activity, -self.threshold, self.threshold)
        return metabolism_activity

