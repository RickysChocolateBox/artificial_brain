import numpy as np

class SynapticVesiclePrimingRegulation:
    def __init__(self, priming_rate, learning_rate, activation_function, threshold):
        self.priming_rate = priming_rate
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

    def update_priming_level(self, priming_level, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in priming level based on the priming rate and activity level
        change_in_priming_level = self.priming_rate * activity_level

        # Update the priming level based on the learning rate and change in priming level
        priming_level += self.learning_rate * change_in_priming_level

        # Ensure that the priming level remains within the specified threshold
        priming_level = np.clip(priming_level, -self.threshold, self.threshold)

        return priming_level

