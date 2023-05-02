import numpy as np

class LocalProteinSynthesisModulation:
    def __init__(self, protein_synthesis_rate, learning_rate, threshold, activation_function='sigmoid'):
        self.protein_synthesis_rate = protein_synthesis_rate
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.activation_function = activation_function

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_protein_synthesis(self, protein_synthesis_level, activity_level):
        # Apply the activation function to activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the protein synthesis change based on activity levels and protein synthesis rate
        protein_synthesis_change = self.learning_rate * self.protein_synthesis_rate * activity_level

        # Update protein synthesis level
        protein_synthesis_level += protein_synthesis_change

        # Apply threshold to protein synthesis level
        protein_synthesis_level = np.minimum(protein_synthesis_level, self.threshold)

        return protein_synthesis_level

