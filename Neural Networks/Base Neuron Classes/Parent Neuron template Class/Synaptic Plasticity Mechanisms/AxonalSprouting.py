import numpy as np

class AxonalSprouting:
    def __init__(self, sprouting_rate, modulation_threshold, noise_std_dev):
        self.sprouting_rate = sprouting_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update axonal sprouting based on activity level
    def update_sprouting(self, sprouting_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update sprouting state based on activity level
        if activity_level >= self.modulation_threshold:
            sprouting_state += self.sprouting_rate
        else:
            sprouting_state -= self.sprouting_rate

        return sprouting_state

# This class represents the mechanism of axonal sprouting. The primary function, update_sprouting, updates the axonal sprouting state based on the activity level and random noise. The sprouting state is increased or decreased according to the sprouting_rate depending on whether the activity level is above or below the modulation_threshold.