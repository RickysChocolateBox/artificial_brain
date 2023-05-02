import numpy as np

class AstrocyteFunctionChanges:
    def __init__(self, astrocyte_rate, learning_rate, activation_function, threshold):
        self.astrocyte_rate = astrocyte_rate
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

    def update_astrocyte_function(self, astrocyte_function, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in astrocyte function based on the astrocyte rate and activity level
        change_in_astrocyte_function = self.astrocyte_rate * activity_level

        # Update the astrocyte function based on the learning rate and change in astrocyte function
        astrocyte_function += self.learning_rate * change_in_astrocyte_function

        # Ensure that the astrocyte function remains within the specified threshold
        astrocyte_function = np.clip(astrocyte_function, -self.threshold, self.threshold)

        return astrocyte_function

