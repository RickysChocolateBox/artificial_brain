import numpy as np

class ChangesInExtracellularMatrixMolecules:
    def __init__(self, num_molecules, learning_rate, activation_function, matrix_rate, threshold):
        self.num_molecules = num_molecules
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.matrix_rate = matrix_rate
        self.threshold = threshold
        self.molecule_activity = np.random.rand(num_molecules)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_matrix_molecule_activity(self, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update molecule activity based on the learning rate, matrix rate, and activity level
        delta_molecule_activity = self.learning_rate * self.matrix_rate * activity
        self.molecule_activity += delta_molecule_activity

        # Ensure that the molecule activity remains within the specified threshold
        self.molecule_activity = np.clip(self.molecule_activity, 0, self.threshold)

        return self.molecule_activity

    def get_molecule_activity(self):
        return self.molecule_activity

