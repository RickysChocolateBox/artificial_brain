import numpy as np
class GABASOM:
    def __init__(self, inhibitory_factor):
        self.inhibitory_factor = inhibitory_factor

    def weaken_connections(self, weights, winners):
        distance = np.linalg.norm(weights - weights[winners], axis=1)
        strength = 1 / (1 + np.exp(self.inhibitory_factor * (distance - np.mean(distance))))
        weakened_weights = weights * strength[:, np.newaxis]

        return weakened_weights
