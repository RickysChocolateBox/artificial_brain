import numpy as np

class ExtracellularVesicleSignaling:
    def __init__(self, signaling_modulation_rate, modulation_threshold, noise_std_dev):
        self.signaling_modulation_rate = signaling_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update extracellular vesicle-mediated signaling based on activity level and noise
    def update_signaling(self, signaling, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update signaling based on activity level
        if activity_level >= self.modulation_threshold:
            signaling += self.signaling_modulation_rate
        else:
            signaling -= self.signaling_modulation_rate

        return signaling

