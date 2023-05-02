import numpy as np

class ExtracellularPotassiumChanges:
    def __init__(self, potassium_rate, learning_rate, activation_function, threshold):
        self.potassium_rate = potassium_rate
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

    # Update extracellular potassium levels based on neural activity
    def update_potassium_levels(self, potassium_levels, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in potassium levels based on the potassium rate and activity level
        change_in_potassium = self.potassium_rate * activity_level

        # Update the potassium levels based on the learning rate and change in potassium
        potassium_levels += self.learning_rate * change_in_potassium

        # Ensure that the potassium levels remain within the specified threshold
        potassium_levels = np.clip(potassium_levels, -self.threshold, self.threshold)

        return potassium_levels

