import numpy as np

class MicrogliaFunctionChanges:
    def __init__(self, microglia_rate, learning_rate, activation_function, threshold):
        self.microglia_rate = microglia_rate
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

    def update_microglia_function(self, microglia_function, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in microglia function based on the microglia rate and activity level
        change_in_microglia_function = self.microglia_rate * activity_level

        # Update the microglia function based on the learning rate and change in microglia function
        microglia_function += self.learning_rate * change_in_microglia_function

        # Ensure that the microglia function remains within the specified threshold
        microglia_function = np.clip(microglia_function, -self.threshold, self.threshold)

        return microglia_function

