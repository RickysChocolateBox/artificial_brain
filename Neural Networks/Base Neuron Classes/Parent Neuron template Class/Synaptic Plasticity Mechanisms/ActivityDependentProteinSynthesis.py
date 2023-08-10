import numpy as np

class ActivityDependentProteinSynthesis:
    def __init__(self, num_proteins, learning_rate, activation_function, synthesis_rate, threshold):
        self.num_proteins = num_proteins
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.synthesis_rate = synthesis_rate
        self.threshold = threshold
        self.protein_activity = np.random.rand(num_proteins)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_protein_activity(self, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update protein activity based on the learning rate, synthesis rate, and activity level
        delta_protein_activity = self.learning_rate * self.synthesis_rate * activity
        self.protein_activity += delta_protein_activity

        # Ensure that the protein activity remains within the specified threshold
        self.protein_activity = np.clip(self.protein_activity, 0, self.threshold)

        return self.protein_activity

    def get_protein_activity(self):
        return self.protein_activity

