import numpy as np

class SynapticVesiclePoolSizeRegulation:
    def __init__(self, pool_size_rate, learning_rate, activation_function, threshold):
        self.pool_size_rate = pool_size_rate
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

    def update_pool_size(self, pool_size, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in pool size based on the pool size rate and activity level
        change_in_pool_size = self.pool_size_rate * activity_level

        # Update the pool size based on the learning rate and change in pool size
        pool_size += self.learning_rate * change_in_pool_size

        # Ensure that the pool size remains within the specified threshold
        pool_size = np.clip(pool_size, -self.threshold, self.threshold)

        return pool_size

