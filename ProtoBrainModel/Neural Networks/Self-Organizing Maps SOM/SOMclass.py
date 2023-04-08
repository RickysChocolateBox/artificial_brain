import numpy as np

class SOM:
    def __init__(self, input_dim, map_size, sigma=1.0, learning_rate=0.5, max_iter=100):
        self.input_dim = input_dim
        self.map_size = map_size
        self.sigma = sigma
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = np.random.random((map_size[0], map_size[1], input_dim))

    def _euclidean_distance(self, x, y):
        return np.linalg.norm(x - y)

    def _find_best_matching_unit(self, input_vector):
        bmu_idx = (0, 0)
        min_dist = float('inf')

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                weight = self.weights[i, j, :]
                dist = self._euclidean_distance(input_vector, weight)

                if dist < min_dist:
                    min_dist = dist
                    bmu_idx = (i, j)

        return bmu_idx

    def _update_weights(self, input_vector, bmu_idx, iteration):
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                weight = self.weights[i, j, :]
                dist = self._euclidean_distance(np.array([i, j]), np.array(bmu_idx))

                if dist <= self.sigma:
                    influence = np.exp(-(dist ** 2) / (2 * (self.sigma ** 2)))
                    self.weights[i, j, :] += influence * self.learning_rate * (input_vector - weight)

    def train(self, data):
        for iteration in range(self.max_iter):
            input_vector = data[np.random.randint(0, len(data))]
            bmu_idx = self._find_best_matching_unit(input_vector)
            self._update_weights(input_vector, bmu_idx, iteration)


