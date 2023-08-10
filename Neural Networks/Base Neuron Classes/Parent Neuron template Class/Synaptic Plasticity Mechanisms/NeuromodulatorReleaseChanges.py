import numpy as np

class NeuromodulatorReleaseChanges:
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

    def update_neuromodulator_release(self, neuromodulator_release, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the altered neuromodulator release based on the release rate and activity level
        altered_neuromodulator_release = self.release_rate * activity_level

        # Update neuromodulator release based on the learning rate and altered neuromodulator release
        neuromodulator_release += self.learning_rate * altered_neuromodulator_release

        # Ensure that the neuromodulator release remains within the specified threshold
        neuromodulator_release = np.clip(neuromodulator_release, -self.threshold, self.threshold)

        return neuromodulator_release

