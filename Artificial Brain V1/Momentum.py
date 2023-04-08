import numpy as np

class OptimizationAlgorithmBaseClass:
    def update_weights(self, weights, gradients):
        raise NotImplementedError("update_weights method should be implemented by subclasses.")

class Momentum(OptimizationAlgorithmBaseClass):
    def __init__(self, learning_rate, momentum):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.velocity = None

    def update_weights(self, weights, gradients):
        if self.velocity is None:
            self.velocity = np.zeros_like(weights)

        self.velocity = self.momentum * self.velocity + self.learning_rate * gradients
        return weights - self.velocity

