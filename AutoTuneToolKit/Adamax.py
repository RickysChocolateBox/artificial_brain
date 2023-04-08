import numpy as np

class OptimizationAlgorithmBaseClass:
    def update_weights(self, weights, gradients):
        raise NotImplementedError("update_weights method should be implemented by subclasses.")


class Adamax(OptimizationAlgorithmBaseClass):
    def __init__(self, learning_rate=0.002, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def update_weights(self, weights, gradients):
        if self.m is None:
            self.m = np.zeros_like(weights)
            self.v = np.zeros_like(weights)

        self.t += 1
        self.m = self.beta1 * self.m + (1 - self.beta1) * gradients
        self.v = np.maximum(self.beta2 * self.v, np.abs(gradients))
        m_hat = self.m / (1 - self.beta1**self.t)
        delta_weights = -self.learning_rate * m_hat / (self.v + self.epsilon)
        return weights + delta_weights

