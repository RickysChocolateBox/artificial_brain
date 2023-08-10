import numpy as np

class HomeostaticSynapticPlasticity:
    def __init__(self, homeostatic_rate, target_activity, learning_rate, noise_std_dev):
        self.homeostatic_rate = homeostatic_rate
        self.target_activity = target_activity
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_synaptic_strength(self, synaptic_strength, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        homeostatic_factor = self.target_activity - activity_level
        synaptic_strength += self.learning_rate * self.homeostatic_rate * homeostatic_factor

        return synaptic_strength

