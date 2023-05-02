import numpy as np

class AxonGuidanceChanges:
    def __init__(self, guidance_rate, learning_rate, activation_function, threshold):
        self.guidance_rate = guidance_rate
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

    def update_axon_guidance(self, axon_guidance, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in axon guidance based on the guidance rate and activity level
        change_in_axon_guidance = self.guidance_rate * activity_level

        # Update the axon guidance based on the learning rate and change in axon guidance
        axon_guidance += self.learning_rate * change_in_axon_guidance

        # Ensure that the axon guidance remains within the specified threshold
        axon_guidance = np.clip(axon_guidance, -self.threshold, self.threshold)

        return axon_guidance

