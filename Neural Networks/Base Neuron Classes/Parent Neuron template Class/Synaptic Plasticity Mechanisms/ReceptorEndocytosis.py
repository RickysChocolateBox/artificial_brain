import numpy as np

class ReceptorEndocytosis:
    def __init__(self, endocytosis_rate, activation_function='sigmoid'):
        self.endocytosis_rate = endocytosis_rate
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

    def update_receptor_internalization(self, receptor_count, activity_levels):
        activity_levels = self.apply_activation_function(activity_levels)
        receptor_internalization = self.endocytosis_rate * activity_levels
        receptor_count -= receptor_internalization
        receptor_count = np.maximum(0, receptor_count)
        return receptor_count

