import numpy as np

class ModulationPresynapticFunction:
    def __init__(self, modulation_rate, learning_rate, activation_function, threshold):
        self.modulation_rate = modulation_rate
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

    def update_presynaptic_function(self, presynaptic_function, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in presynaptic function based on the modulation rate and activity level
        change_in_presynaptic_function = self.modulation_rate * activity_level

        # Update the presynaptic function based on the learning rate and change in presynaptic function
        presynaptic_function += self.learning_rate * change_in_presynaptic_function

        # Ensure that the presynaptic function remains within the specified threshold
        presynaptic_function = np.clip(presynaptic_function, -self.threshold, self.threshold)

        return presynaptic_function

