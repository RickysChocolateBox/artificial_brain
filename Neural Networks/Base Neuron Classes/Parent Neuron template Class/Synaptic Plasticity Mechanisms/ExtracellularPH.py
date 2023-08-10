import numpy as np

class ExtracellularPH:
    def __init__(self, ph_change_rate, ph_threshold, noise_std_dev):
        self.ph_change_rate = ph_change_rate
        self.ph_threshold = ph_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update extracellular pH based on activity level and noise
    def update_ph(self, extracellular_ph, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update extracellular pH based on activity level
        if activity_level >= self.ph_threshold:
            extracellular_ph += self.ph_change_rate
        else:
            extracellular_ph -= self.ph_change_rate

        return extracellular_ph

