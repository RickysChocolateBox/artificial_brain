import numpy as np

class DendriticArborizationChanges:
    def __init__(self, arborization_rate, learning_rate, activation_function, threshold):
        self.arborization_rate = arborization_rate
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

    def update_dendritic_arborization(self, arborization, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_arborization = self.arborization_rate * activity_level
        arborization += self.learning_rate * change_in_arborization
        arborization = np.clip(arborization, -self.threshold, self.threshold)
        return arborization

