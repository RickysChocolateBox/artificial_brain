import numpy as np

class PresynapticCalciumInflux:
    def __init__(self, calcium_modulation_rate, modulation_threshold, noise_std_dev):
        self.calcium_modulation_rate = calcium_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update calcium influx modulation based on activity level and noise
    def update_calcium_influx_modulation(self, calcium_influx, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update calcium influx modulation based on activity level
        if activity_level >= self.modulation_threshold:
            calcium_influx += self.calcium_modulation_rate
        else:
            calcium_influx -= self.calcium_modulation_rate

        return calcium_influx

