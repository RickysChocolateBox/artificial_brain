import numpy as np

class ReceptorPhosphorylationChanges:
    def __init__(self, phosphorylation_rate, learning_rate, activation_function, threshold):
        self.phosphorylation_rate = phosphorylation_rate
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

    def update_receptor_phosphorylation(self, phosphorylation_level, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_phosphorylation = self.phosphorylation_rate * activity_level
        phosphorylation_level += self.learning_rate * change_in_phosphorylation
        phosphorylation_level = np.clip(phosphorylation_level, -self.threshold, self.threshold)
        return phosphorylation_level

