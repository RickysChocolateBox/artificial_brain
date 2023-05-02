import numpy as np

class InhibitionOfNeurotransmitterRelease:
    def __init__(self, inhibition_rate, learning_rate, activation_function, threshold):
        self.inhibition_rate = inhibition_rate
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

    def update_inhibition_level(self, inhibition_level, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_inhibition_level = self.inhibition_rate * activity_level
        inhibition_level += self.learning_rate * change_in_inhibition_level
        inhibition_level = np.clip(inhibition_level, -self.threshold, self.threshold)
        return inhibition_level

