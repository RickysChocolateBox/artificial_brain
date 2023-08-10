import numpy as np

class PostsynapticDensityStructureModulation:
    def __init__(self, structure_rate, learning_rate, activation_function, threshold):
        self.structure_rate = structure_rate
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

    def update_postsynaptic_density_structure(self, postsynaptic_density_structure, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in postsynaptic density structure based on the structure rate and activity level
        change_in_structure = self.structure_rate * activity_level

        # Update the postsynaptic density structure based on the learning rate and change in structure
        postsynaptic_density_structure += self.learning_rate * change_in_structure

        # Ensure that the postsynaptic density structure remains within the specified threshold
        postsynaptic_density_structure = np.clip(postsynaptic_density_structure, -self.threshold, self.threshold)

        return postsynaptic_density_structure

