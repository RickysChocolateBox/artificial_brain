import numpy as np

class SynapticCleftDimensionsChanges:
    def __init__(self, dimension_rate, learning_rate, activation_function, threshold):
        self.dimension_rate = dimension_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.threshold = threshold

    # Define the sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Define the rectified linear unit (ReLU) activation function
    def relu(self, x):
        return np.maximum(0, x)

    # Apply the specified activation function
    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    # Update synaptic cleft dimensions based on neural activity
    def update_cleft_dimensions(self, cleft_dimensions, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in cleft dimensions based on the dimension rate and activity level
        change_in_dimensions = self.dimension_rate * activity_level

        # Update the cleft dimensions based on the learning rate and change in dimensions
        cleft_dimensions += self.learning_rate * change_in_dimensions

        # Ensure that the cleft dimensions remain within the specified threshold
        cleft_dimensions = np.clip(cleft_dimensions, -self.threshold, self.threshold)

        return cleft_dimensions

