import numpy as np

class ExtracellularGlutamateChanges:
    def __init__(self, glutamate_rate, learning_rate, activation_function, threshold):
        self.glutamate_rate = glutamate_rate
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

    # Update extracellular glutamate levels based on neural activity
    def update_glutamate_levels(self, glutamate_levels, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in glutamate levels based on the glutamate rate and activity level
        change_in_glutamate = self.glutamate_rate * activity_level

        # Update the glutamate levels based on the learning rate and change in glutamate
        glutamate_levels += self.learning_rate * change_in_glutamate

        # Ensure that the glutamate levels remain within the specified threshold
        glutamate_levels = np.clip(glutamate_levels, -self.threshold, self.threshold)

        return glutamate_levels

