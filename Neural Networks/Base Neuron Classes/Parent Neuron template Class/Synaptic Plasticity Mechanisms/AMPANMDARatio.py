import numpy as np

class AMPANMDARatio:
    def __init__(self, ratio_rate, ratio_threshold, noise_std_dev):
        self.ratio_rate = ratio_rate
        self.ratio_threshold = ratio_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update AMPA/NMDA receptor ratio
    def update_ratio(self, ratio_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update ratio state based on activity level
        if activity_level >= self.ratio_threshold:
            ratio_state += self.ratio_rate
        else:
            ratio_state -= self.ratio_rate

        return ratio_state

# This class represents the mechanism of changes in AMPA/NMDA receptor ratio. The primary function, update_ratio, updates the AMPA/NMDA receptor ratio state based on the activity level and random noise. The ratio state is increased or decreased according to the ratio_rate depending on whether the activity level is above or below the ratio_threshold.