import numpy as np

class CytoskeletalDynamics:
    def __init__(self, learning_rate, dynamics_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.dynamics_threshold = dynamics_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the cytoskeletal dynamics based on activity level and noise
    def update_cytoskeletal_dynamics(self, dynamics_rate, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update dynamics rate based on activity level
        if activity_level >= self.dynamics_threshold:
            dynamics_rate += self.learning_rate * (1 - dynamics_rate)
        else:
            dynamics_rate -= self.learning_rate * dynamics_rate

        return dynamics_rate

