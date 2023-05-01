import numpy as np

class SynapticScaling:
    def __init__(self, scaling_rate, target_activity, learning_rate, noise_std_dev):
        self.scaling_rate = scaling_rate
        self.target_activity = target_activity
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_synaptic_strength(self, synaptic_strength, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        scaling_factor = self.target_activity / (activity_level + 1e-8)
        synaptic_strength += self.learning_rate * self.scaling_rate * (scaling_factor - 1)

        return synaptic_strength

