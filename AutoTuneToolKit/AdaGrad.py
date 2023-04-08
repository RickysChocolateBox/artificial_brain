import numpy as np

class OptimizationAlgorithmBaseClass:
    def update_weights(self, weights, gradients):
        raise NotImplementedError("update_weights method should be implemented by subclasses.")

class AdaGrad(OptimizationAlgorithmBaseClass):
    def __init__(self, learning_rate, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.cache = None

    def update_weights(self, weights, gradients):
        if self.cache is None:
            self.cache = np.zeros_like(weights)

        self.cache += gradients ** 2
        return weights - self.learning_rate * gradients / (np.sqrt(self.cache) + self.epsilon)

