import numpy as np

class PresynapticCalciumDynamics:
    def __init__(self, calcium_rate, learning_rate, activation_function, threshold):
        self.calcium_rate = calcium_rate
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

    # Update presynaptic calcium dynamics based on neural activity
    def update_calcium_dynamics(self, calcium_level, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in calcium level based on the calcium rate and activity level
        change_in_calcium = self.calcium_rate * activity_level

        # Update the calcium level based on the learning rate and change in calcium
        calcium_level += self.learning_rate * change_in_calcium

        # Ensure that the calcium level remains within the specified threshold
        calcium_level = np.clip(calcium_level, -self.threshold, self.threshold)

        return calcium_level

