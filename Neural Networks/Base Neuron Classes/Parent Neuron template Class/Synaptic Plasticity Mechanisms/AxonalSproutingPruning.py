import numpy as np

class AxonalSproutingPruning:
    def __init__(self, sprouting_rate, pruning_rate, sprouting_threshold, pruning_threshold,
                 max_axonal_density, min_axonal_density, learning_rate, noise_std_dev):
        self.sprouting_rate = sprouting_rate
        self.pruning_rate = pruning_rate
        self.sprouting_threshold = sprouting_threshold
        self.pruning_threshold = pruning_threshold
        self.max_axonal_density = max_axonal_density
        self.min_axonal_density = min_axonal_density
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_axonal_density(self, axonal_density, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        if activity_level >= self.sprouting_threshold:
            axonal_density += self.learning_rate * self.sprouting_rate
        elif activity_level <= self.pruning_threshold:
            axonal_density -= self.learning_rate * self.pruning_rate

        axonal_density = np.clip(axonal_density, self.min_axonal_density, self.max_axonal_density)
        return axonal_density


