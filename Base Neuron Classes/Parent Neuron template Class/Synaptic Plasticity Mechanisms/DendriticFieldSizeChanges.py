import numpy as np

class DendriticFieldSizeChanges:
    def __init__(self, field_size_rate, learning_rate, activation_function, threshold):
        self.field_size_rate = field_size_rate
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

    def update_dendritic_field_size(self, field_size, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_field_size = self.field_size_rate * activity_level
        field_size += self.learning_rate * change_in_field_size
        field_size = np.clip(field_size, -self.threshold, self.threshold)
        return field_size

