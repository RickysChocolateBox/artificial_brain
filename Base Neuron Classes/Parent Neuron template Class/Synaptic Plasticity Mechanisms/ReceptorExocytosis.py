import numpy as np

class ReceptorExocytosis:
    def __init__(self, exocytosis_rate, activation_function='sigmoid'):
        self.exocytosis_rate = exocytosis_rate
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

    def update_receptor_insertion(self, receptor_count, activity_levels):
        activity_levels = self.apply_activation_function(activity_levels)
        receptor_insertion = self.exocytosis_rate * activity_levels
        receptor_count += receptor_insertion
        return receptor_count

