import numpy as np

class AlteredNeuropeptideRelease:
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

    def update_neuropeptide_release(self, neuropeptide_release, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in neuropeptide release based on the release rate and activity level
        change_in_release = self.release_rate * activity_level

        # Update the neuropeptide release based on the learning rate and change in release
        neuropeptide_release += self.learning_rate * change_in_release

        # Ensure that the neuropeptide release remains within the specified threshold
        neuropeptide_release = np.clip(neuropeptide_release, -self.threshold, self.threshold)

        return neuropeptide_release
