import numpy as np

class IntrinsicPlasticity:
    def __init__(self, learning_rate, ip_rate, noise_std_dev):
        self.learning_rate = learning_rate
        self.ip_rate = ip_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_intrinsic_excitability(self, intrinsic_excitability, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        intrinsic_excitability += self.learning_rate * self.ip_rate * activity_level

        return intrinsic_excitability

