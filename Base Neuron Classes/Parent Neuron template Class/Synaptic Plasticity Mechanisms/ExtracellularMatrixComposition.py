import numpy as np

class ExtracellularMatrixComposition:
    def __init__(self, matrix_change_rate, change_threshold, noise_std_dev):
        self.matrix_change_rate = matrix_change_rate
        self.change_threshold = change_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update extracellular matrix composition based on activity level and noise
    def update_matrix_composition(self, matrix_composition, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update matrix composition based on activity level
        if activity_level >= self.change_threshold:
            matrix_composition += self.matrix_change_rate
        else:
            matrix_composition -= self.matrix_change_rate

        return matrix_composition

