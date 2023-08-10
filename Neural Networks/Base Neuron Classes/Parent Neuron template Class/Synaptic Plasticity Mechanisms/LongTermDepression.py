import numpy as np

class LongTermDepression:
    def __init__(self, depression_rate, learning_rate, activation_function, threshold):
        self.depression_rate = depression_rate
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

    def induce_ltd(self, synaptic_weights, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_weights = -self.depression_rate * activity_level
        synaptic_weights += self.learning_rate * change_in_weights
        synaptic_weights = np.clip(synaptic_weights, -self.threshold, self.threshold)
        return synaptic_weights
