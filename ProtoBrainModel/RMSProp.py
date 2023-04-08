import numpy as np

class OptimizationAlgorithmBaseClass:
    def update_weights(self, weights, gradients):
        raise NotImplementedError("update_weights method should be implemented by subclasses.")


class RMSProp(OptimizationAlgorithmBaseClass):
    def __init__(self, learning_rate=0.001, rho=0.9, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.rho = rho
        self.epsilon = epsilon
        self.cache = None

    def update_weights(self, weights, gradients):
        if self.cache is None:
            self.cache = np.zeros_like(weights)

        self.cache = self.rho * self.cache + (1 - self.rho) * gradients**2
        delta_weights = -self.learning_rate * gradients / (np.sqrt(self.cache) + self.epsilon)
        return weights + delta_weights

