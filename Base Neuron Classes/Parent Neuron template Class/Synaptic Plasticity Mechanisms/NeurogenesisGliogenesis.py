import numpy as np

class NeurogenesisGliogenesis:
    def __init__(self, neurogenesis_rate, gliogenesis_rate, max_cell_count, learning_rate, noise_std_dev):
        self.neurogenesis_rate = neurogenesis_rate
        self.gliogenesis_rate = gliogenesis_rate
        self.max_cell_count = max_cell_count
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_cell_count(self, cell_count, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        cell_count += self.learning_rate * (self.neurogenesis_rate - self.gliogenesis_rate) * activity_level
        cell_count = min(cell_count, self.max_cell_count)

        return cell_count

