import numpy as np

class IntracellularPHChanges:
    def __init__(self, ph_rate, learning_rate, activation_function, threshold):
        self.ph_rate = ph_rate
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

    def update_ph_level(self, ph_level, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_ph_level = self.ph_rate * activity_level
        ph_level += self.learning_rate * change_in_ph_level
        ph_level = np.clip(ph_level, -self.threshold, self.threshold)
        return ph_level

