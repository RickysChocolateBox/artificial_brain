import numpy as np

class :
    def __init__(self, camkii_rate, learning_rate, activation_function, threshold):
        self.camkii_rate = camkii_rate
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

    def update_camkii_activity(self, camkii_activity, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_camkii_activity = self.camkii_rate * activity_level
        camkii_activity += self.learning_rate * change_in_camkii_activity
        camkii_activity = np.clip(camkii_activity, -self.threshold, self.threshold)
        return camkii_activity

