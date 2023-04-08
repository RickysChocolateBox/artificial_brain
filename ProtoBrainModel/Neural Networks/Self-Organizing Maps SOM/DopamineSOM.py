import numpy as np

class DopamineSOM:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def update_weights(self, input_vector, weights):
        winners = np.argmin(np.linalg.norm(weights - input_vector, axis=1))
        delta_weights = self.learning_rate * (input_vector - weights)
        weights += delta_weights

        return weights, winners

