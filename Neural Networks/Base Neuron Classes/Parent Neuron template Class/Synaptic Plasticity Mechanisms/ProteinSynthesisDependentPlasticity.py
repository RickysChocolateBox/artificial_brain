import numpy as np

class ProteinSynthesisDependentPlasticity:
    def __init__(self, synthesis_rate, activation_threshold, decay_rate, learning_rate, activation_function='sigmoid'):
        self.synthesis_rate = synthesis_rate
        self.activation_threshold = activation_threshold
        self.decay_rate = decay_rate
        self.learning_rate = learning_rate
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

    def update_protein_levels(self, protein_levels, activity_levels):
        # Apply the activation function to activity levels
        activity_levels = self.apply_activation_function(activity_levels)

        # Calculate protein synthesis based on activity levels and synthesis rate
        protein_synthesis = self.learning_rate * self.synthesis_rate * activity_levels

        # Update protein levels based on synthesis and decay rates
        protein_levels += protein_synthesis
        protein_levels *= (1 - self.decay_rate)

        # Apply activation threshold to protein levels
        protein_levels = np.maximum(protein_levels, self.activation_threshold)

        return protein_levels

