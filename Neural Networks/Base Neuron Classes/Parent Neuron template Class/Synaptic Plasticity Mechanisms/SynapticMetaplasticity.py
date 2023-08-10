import numpy as np

class SynapticMetaplasticity:
    def __init__(self, learning_rate, metaplasticity_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.metaplasticity_threshold = metaplasticity_threshold
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_metaplasticity(self, synaptic_weight, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        if activity_level >= self.metaplasticity_threshold:
            synaptic_weight += self.learning_rate * (1 - synaptic_weight)
        else:
            synaptic_weight -= self.learning_rate * synaptic_weight

        return synaptic_weight


