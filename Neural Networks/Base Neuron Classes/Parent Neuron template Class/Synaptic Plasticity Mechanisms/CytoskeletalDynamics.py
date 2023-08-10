import numpy as np

class CytoskeletalDynamics:
    def __init__(self, filaments, learning_rate, activation_function, dynamics_rate, threshold):
        self.filaments = filaments
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.dynamics_rate = dynamics_rate
        self.threshold = threshold
        self.filament_activity = np.random.rand(filaments)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_cytoskeletal_dynamics(self, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update filament activity based on the learning rate, dynamics rate, and activity level
        delta_filament_activity = self.learning_rate * self.dynamics_rate * activity
        self.filament_activity += delta_filament_activity

        # Ensure that the filament activity remains within the specified threshold
        self.filament_activity = np.clip(self.filament_activity, 0, self.threshold)

        return self.filament_activity

    def get_filament_activity(self):
        return self.filament_activity

