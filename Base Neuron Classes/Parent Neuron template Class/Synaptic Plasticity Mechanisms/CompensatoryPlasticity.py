import numpy as np

class CompensatoryPlasticity:
    def __init__(self, learning_rate, cp_rate, target_activity, noise_std_dev):
        self.learning_rate = learning_rate
        self.cp_rate = cp_rate
        self.target_activity = target_activity
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_compensatory_strength(self, compensatory_strength, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        compensatory_strength += self.learning_rate * self.cp_rate * (self.target_activity - activity_level)

        return compensatory_strength

