import numpy as np

class ActiveZoneComposition:
    def __init__(self, composition_modulation_rate, modulation_threshold, noise_std_dev):
        self.composition_modulation_rate = composition_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update active zone composition based on activity level and noise
    def update_composition(self, composition_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update composition state based on activity level
        if activity_level >= self.modulation_threshold:
            composition_state += self.composition_modulation_rate
        else:
            composition_state -= self.composition_modulation_rate

        return composition_state

