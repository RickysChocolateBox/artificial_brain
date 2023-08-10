import numpy as np

class EpigeneticModifications:
    def __init__(self, modification_rate, learning_rate, noise_std_dev):
        self.modification_rate = modification_rate
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_modifications(self, modification_level, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        modification_level += self.learning_rate * self.modification_rate * activity_level

        return modification_level

