import numpy as np

class NeuronalMorphologyChanges:
    def __init__(self, morphology_rate, learning_rate, activation_function, threshold):
        self.morphology_rate = morphology_rate
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

    # Update neuronal morphology based on neural activity
    def update_neuronal_morphology(self, neuronal_morphology, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in neuronal morphology based on the morphology rate and activity level
        change_in_morphology = self.morphology_rate * activity_level

        # Update the neuronal morphology based on the learning rate and change in morphology
        neuronal_morphology += self.learning_rate * change_in_morphology

        # Ensure that the neuronal morphology remains within the specified threshold
        neuronal_morphology = np.clip(neuronal_morphology, -self.threshold, self.threshold)

        return neuronal_morphology
