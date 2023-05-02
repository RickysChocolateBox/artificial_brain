import numpy as np

class SpontaneousNeurotransmitterRelease:
    def __init__(self, release_rate, learning_rate, activation_function, threshold):
        self.release_rate = release_rate
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

    def update_spontaneous_release(self, spontaneous_release, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in spontaneous release based on the release rate and activity level
        change_in_spontaneous_release = self.release_rate * activity_level

        # Update the spontaneous release based on the learning rate and change in spontaneous release
        spontaneous_release += self.learning_rate * change_in_spontaneous_release

        # Ensure that the spontaneous release remains within the specified threshold
        spontaneous_release = np.clip(spontaneous_release, -self.threshold, self.threshold)

        return spontaneous_release

