import numpy as np
class DopamineFNN:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def adjust_weights(self, weights, inputs, error):
        delta_weights = self.learning_rate * error * inputs
        return weights + delta_weights
