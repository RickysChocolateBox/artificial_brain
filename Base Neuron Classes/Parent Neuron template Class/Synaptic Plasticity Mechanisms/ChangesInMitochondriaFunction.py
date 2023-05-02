import numpy as np

class ChangesInMitochondriaFunction:
    def __init__(self, num_mitochondria, learning_rate, activation_function, function_rate, threshold):
        self.num_mitochondria = num_mitochondria
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.function_rate = function_rate
        self.threshold = threshold
        self.mitochondria_activity = np.random.rand(num_mitochondria)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_mitochondria_activity(self, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update mitochondria activity based on the learning rate, function rate, and activity level
        delta_mitochondria_activity = self.learning_rate * self.function_rate * activity
        self.mitochondria_activity += delta_mitochondria_activity

        # Ensure that the mitochondria activity remains within the specified threshold
        self.mitochondria_activity = np.clip(self.mitochondria_activity, 0, self.threshold)

        return self.mitochondria_activity

    def get_mitochondria_activity(self):
        return self.mitochondria_activity

