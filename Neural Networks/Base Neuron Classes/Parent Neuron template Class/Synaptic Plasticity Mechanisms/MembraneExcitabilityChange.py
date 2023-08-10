import numpy as np

class MembraneExcitabilityChange:
    def __init__(self, excitability_rate, learning_rate, noise_std_dev):
        self.excitability_rate = excitability_rate
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_excitability(self, membrane_excitability, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        membrane_excitability += self.learning_rate * self.excitability_rate * activity_level

        return membrane_excitability

