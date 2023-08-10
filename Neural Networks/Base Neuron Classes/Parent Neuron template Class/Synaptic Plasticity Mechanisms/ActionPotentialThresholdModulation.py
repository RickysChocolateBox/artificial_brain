import numpy as np

class ActionPotentialThresholdModulation:
    def __init__(self, threshold_rate, learning_rate, activation_function, threshold_range):
        self.threshold_rate = threshold_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.threshold_range = threshold_range

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_threshold(self, action_potential_threshold, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in action potential threshold based on the threshold rate and activity level
        change_in_threshold = self.threshold_rate * activity_level

        # Update the action potential threshold based on the learning rate and change in threshold
        action_potential_threshold += self.learning_rate * change_in_threshold

        # Ensure that the action potential threshold remains within the specified threshold range
        action_potential_threshold = np.clip(action_potential_threshold, self.threshold_range[0], self.threshold_range[1])

        return action_potential_threshold

