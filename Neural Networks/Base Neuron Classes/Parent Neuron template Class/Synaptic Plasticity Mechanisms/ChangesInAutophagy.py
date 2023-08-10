import numpy as np

class ChangesInAutophagy:
    def __init__(self, autophagy_rate, learning_rate, activation_function, threshold):
        self.autophagy_rate = autophagy_rate
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

    def update_autophagy_level(self, autophagy_level, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update autophagy level based on the autophagy rate, learning rate, and activity level
        autophagy_level += self.learning_rate * self.autophagy_rate * activity

        # Ensure that the autophagy level remains within the specified threshold
        autophagy_level = np.clip(autophagy_level, 0, self.threshold)

        return autophagy_level

