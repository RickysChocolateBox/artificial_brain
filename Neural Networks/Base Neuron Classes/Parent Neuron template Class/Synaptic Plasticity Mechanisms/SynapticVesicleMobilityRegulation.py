import numpy as np

class SynapticVesicleMobilityRegulation:
    def __init__(self, mobility_rate, learning_rate, activation_function, threshold):
        self.mobility_rate = mobility_rate
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

    def update_vesicle_mobility(self, vesicle_mobility, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_mobility = self.mobility_rate * activity_level
        vesicle_mobility += self.learning_rate * change_in_mobility
        vesicle_mobility = np.clip(vesicle_mobility, -self.threshold, self.threshold)
        return vesicle_mobility

