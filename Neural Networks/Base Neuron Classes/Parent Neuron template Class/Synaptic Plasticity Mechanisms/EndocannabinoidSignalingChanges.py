import numpy as np

class EndocannabinoidSignalingChanges:
    def __init__(self, signaling_rate, learning_rate, activation_function, threshold):
        self.signaling_rate = signaling_rate
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

    def update_endocannabinoid_signaling(self, endocannabinoid_signaling, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in endocannabinoid signaling based on the signaling rate and activity level
        change_in_signaling = self.signaling_rate * activity_level

        # Update the endocannabinoid signaling based on the learning rate and change in signaling
        endocannabinoid_signaling += self.learning_rate * change_in_signaling

        # Ensure that the endocannabinoid signaling remains within the specified threshold
        endocannabinoid_signaling = np.clip(endocannabinoid_signaling, -self.threshold, self.threshold)

        return endocannabinoid_signaling

