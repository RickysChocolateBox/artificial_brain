import numpy as np

class SynapticVesicleFusionPoreSize:
    def __init__(self, pore_size_rate, learning_rate, activation_function, threshold):
        self.pore_size_rate = pore_size_rate
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

    def update_pore_size(self, pore_size, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_pore_size = self.pore_size_rate * activity_level
        pore_size += self.learning_rate * change_in_pore_size
        pore_size = np.clip(pore_size, -self.threshold, self.threshold)
        return pore_size

