import numpy as np

class AlterationOfReceptorSensitivity:
    def __init__(self, sensitivity_rate, learning_rate, activation_function, threshold):
        self.sensitivity_rate = sensitivity_rate
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

    def update_receptor_sensitivity(self, receptor_sensitivity, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_sensitivity = self.sensitivity_rate * activity_level
        receptor_sensitivity += self.learning_rate * change_in_sensitivity
        receptor_sensitivity = np.clip(receptor_sensitivity, -self.threshold, self.threshold)
        return receptor_sensitivity

