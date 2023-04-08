import numpy as np

class OptimizationAlgorithmBaseClass:
    def update_weights(self, weights, gradients):
        raise NotImplementedError("update_weights method should be implemented by subclasses.")

class SGD(OptimizationAlgorithmBaseClass):
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def update_weights(self, weights, gradients):
        return weights - self.learning_rate * gradients

