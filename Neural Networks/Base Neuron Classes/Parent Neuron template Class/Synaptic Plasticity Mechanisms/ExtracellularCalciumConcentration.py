import numpy as np

class ExtracellularCalciumConcentration:
    def __init__(self, modulation_rate, modulation_threshold, noise_std_dev):
        self.modulation_rate = modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update extracellular calcium concentration
    def update_concentration(self, concentration_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update concentration state based on activity level
        if activity_level >= self.modulation_threshold:
            concentration_state += self.modulation_rate
        else:
            concentration_state -= self.modulation_rate

        return concentration_state

# This class represents the mechanism of changes in extracellular calcium concentration. The primary function, update_concentration, updates the extracellular calcium concentration state based on the activity level and random noise. The concentration state is increased or decreased according to the modulation_rate depending on whether the activity level is above or below the modulation_threshold.