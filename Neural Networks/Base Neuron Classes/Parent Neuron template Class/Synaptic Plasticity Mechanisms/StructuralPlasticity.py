import numpy as np

class StructuralPlasticity:
    def __init__(self, learning_rate, sp_rate, max_structure, min_structure, noise_std_dev):
        self.learning_rate = learning_rate
        self.sp_rate = sp_rate
        self.max_structure = max_structure
        self.min_structure = min_structure
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_structure(self, structure, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        structure += self.learning_rate * self.sp_rate * activity_level

        structure = np.clip(structure, self.min_structure, self.max_structure)
        return structure

