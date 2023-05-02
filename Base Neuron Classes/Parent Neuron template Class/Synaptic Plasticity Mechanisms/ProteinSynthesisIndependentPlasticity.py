import numpy as np

class ProteinSynthesisIndependentPlasticity:
    def __init__(self, change_rate, learning_rate, activation_threshold, activation_function='sigmoid'):
        self.change_rate = change_rate
        self.learning_rate = learning_rate
        self.activation_threshold = activation_threshold
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

    def update_plasticity(self, plasticity_level, activity_level):
        # Apply the activation function to activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the plasticity change based on activity levels and change rate
        plasticity_change = self.learning_rate * self.change_rate * activity_level

        # Update plasticity level
        plasticity_level += plasticity_change

        # Apply activation threshold to plasticity level
        plasticity_level = np.maximum(plasticity_level, self.activation_threshold)

        return plasticity_level

