import numpy as np

class DendriticSpineMorphologyRegulation:
    def __init__(self, morphology_rate, learning_rate, activation_function, threshold):
        self.morphology_rate = morphology_rate
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

    def update_spine_morphology(self, spine_morphology, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in dendritic spine morphology based on the morphology rate and activity level
        change_in_spine_morphology = self.morphology_rate * activity_level

        # Update the dendritic spine morphology based on the learning rate and change in spine morphology
        spine_morphology += self.learning_rate * change_in_spine_morphology

        # Ensure that the dendritic spine morphology remains within the specified threshold
        spine_morphology = np.clip(spine_morphology, -self.threshold, self.threshold)

        return spine_morphology

