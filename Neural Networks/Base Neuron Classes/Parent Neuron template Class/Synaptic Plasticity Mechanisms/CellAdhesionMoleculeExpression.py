import numpy as np

class CellAdhesionMoleculeExpression:
    def __init__(self, molecule_count, expression_rate, learning_rate, activation_function, threshold):
        self.molecule_count = molecule_count
        self.expression_rate = expression_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.threshold = threshold
        self.molecule_expression = np.random.rand(molecule_count)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_expression(self, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update expression levels based on the learning rate, expression rate, and activity level
        delta_expression = self.learning_rate * self.expression_rate * activity
        self.molecule_expression += delta_expression

        # Ensure that the molecule expression remains within the specified threshold
        self.molecule_expression = np.clip(self.molecule_expression, 0, self.threshold)

        return self.molecule_expression

    def get_molecule_expression(self):
        return self.molecule_expression

