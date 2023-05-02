import numpy as np

class NeurotrophicFactorRegulation:
    def __init__(self, num_factors, learning_rate, activation_function, regulation_rate, threshold):
        self.num_factors = num_factors
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.regulation_rate = regulation_rate
        self.threshold = threshold
        self.factor_activity = np.random.rand(num_factors)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_factor_activity(self, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update factor activity based on the learning rate, regulation rate, and activity level
        delta_factor_activity = self.learning_rate * self.regulation_rate * activity
        self.factor_activity += delta_factor_activity

        # Ensure that the factor activity remains within the specified threshold
        self.factor_activity = np.clip(self.factor_activity, 0, self.threshold)

        return self.factor_activity

    def get_factor_activity(self):
        return self.factor_activity

