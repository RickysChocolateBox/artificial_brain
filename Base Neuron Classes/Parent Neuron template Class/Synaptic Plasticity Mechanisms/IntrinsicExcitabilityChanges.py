import numpy as np

class IntrinsicExcitabilityChanges:
    def __init__(self, excitability_rate, learning_rate, threshold, activation_function):
        self.excitability_rate = excitability_rate
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.activation_function = activation_function

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def update_excitability_level(self, excitability_level, activity_level):
        # Add random noise to activity level
        noise = np.random.normal(0, 0.1)
        activity_level += noise

        # Apply the specified activation function to the activity level
        if self.activation_function == 'sigmoid':
            activity_level = self.sigmoid(activity_level)
        elif self.activation_function == 'relu':
            activity_level = self.relu(activity_level)

        # Update excitability level based on the excitability rate, learning rate, and activity level
        excitability_level += self.learning_rate * self.excitability_rate * activity_level

        # Ensure that the excitability level remains within the specified threshold
        if excitability_level > self.threshold:
            excitability_level = self.threshold
        elif excitability_level < -self.threshold:
            excitability_level = -self.threshold

        return excitability_level

