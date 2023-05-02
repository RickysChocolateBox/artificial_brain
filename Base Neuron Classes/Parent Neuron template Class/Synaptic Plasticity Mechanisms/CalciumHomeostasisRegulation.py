import numpy as np

class CalciumHomeostasisRegulation:
    def __init__(self, homeostasis_rate, learning_rate, activation_function, threshold):
        self.homeostasis_rate = homeostasis_rate
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

    def update_calcium_homeostasis(self, calcium_homeostasis, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in calcium homeostasis based on the homeostasis rate and activity level
        change_in_homeostasis = self.homeostasis_rate * activity_level

        # Update the calcium homeostasis based on the learning rate and change in homeostasis
        calcium_homeostasis += self.learning_rate * change_in_homeostasis

        # Ensure that the calcium homeostasis remains within the specified threshold
        calcium_homeostasis = np.clip(calcium_homeostasis, -self.threshold, self.threshold)

        return calcium_homeostasis

