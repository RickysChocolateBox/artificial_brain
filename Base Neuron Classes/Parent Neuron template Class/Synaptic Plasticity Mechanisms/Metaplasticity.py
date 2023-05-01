import numpy as np

class Metaplasticity:
    def __init__(self, learning_rate, metaplasticity_rate, noise_std_dev):
        self.learning_rate = learning_rate
        self.metaplasticity_rate = metaplasticity_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_synaptic_threshold(self, synaptic_threshold, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)
        
        synaptic_threshold += self.learning_rate * self.metaplasticity_rate * activity_level

        return synaptic_threshold

