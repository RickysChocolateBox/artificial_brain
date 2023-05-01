import numpy as np

class NeurotransmitterReuptake:
    def __init__(self, reuptake_modulation_rate, modulation_threshold, noise_std_dev):
        self.reuptake_modulation_rate = reuptake_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update neurotransmitter reuptake modulation based on activity level and noise
    def update_reuptake_modulation(self, reuptake_rate, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update reuptake modulation based on activity level
        if activity_level >= self.modulation_threshold:
            reuptake_rate += self.reuptake_modulation_rate
        else:
            reuptake_rate -= self.reuptake_modulation_rate

        return reuptake_rate

