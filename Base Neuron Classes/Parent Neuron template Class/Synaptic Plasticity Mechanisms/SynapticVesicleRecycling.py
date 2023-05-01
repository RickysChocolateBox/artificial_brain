import numpy as np

class SynapticVesicleRecycling:
    def __init__(self, learning_rate, recycling_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.recycling_threshold = recycling_threshold
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_vesicle_recycling(self, recycling_rate, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        if activity_level >= self.recycling_threshold:
            recycling_rate += self.learning_rate * (1 - recycling_rate)
        else:
            recycling_rate -= self.learning_rate * recycling_rate

        return recycling_rate

