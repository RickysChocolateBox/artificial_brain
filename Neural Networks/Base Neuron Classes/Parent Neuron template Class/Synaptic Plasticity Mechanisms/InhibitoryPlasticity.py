import numpy as np

class InhibitoryPlasticity:
    def __init__(self, inhibitory_change_rate, inhibitory_threshold, noise_std_dev):
        self.inhibitory_change_rate = inhibitory_change_rate
        self.inhibitory_threshold = inhibitory_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update inhibitory strength based on activity level and noise
    def update_inhibitory_strength(self, inhibitory_strength, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update inhibitory strength based on activity level
        if activity_level >= self.inhibitory_threshold:
            inhibitory_strength += self.inhibitory_change_rate
        else:
            inhibitory_strength -= self.inhibitory_change_rate

        return inhibitory_strength

