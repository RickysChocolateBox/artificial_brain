import numpy as np

class OptimizationAlgorithmBaseClass:
    def update_weights(self, weights, gradients):
        raise NotImplementedError("update_weights method should be implemented by subclasses.")


class Adadelta(OptimizationAlgorithmBaseClass):
    def __init__(self, rho=0.95, epsilon=1e-8):
        self.rho = rho
        self.epsilon = epsilon
        self.cache = None
        self.delta_cache = None

    def update_weights(self, weights, gradients):
        if self.cache is None:
            self.cache = np.zeros_like(weights)
            self.delta_cache = np.zeros_like(weights)

        self.cache = self.rho * self.cache + (1 - self.rho) * gradients**2
        delta_weights = -np.sqrt(self.delta_cache + self.epsilon) * gradients / np.sqrt(self.cache + self.epsilon)
        self.delta_cache = self.rho * self.delta_cache + (1 - self.rho) * delta_weights**2
        return weights + delta_weights

