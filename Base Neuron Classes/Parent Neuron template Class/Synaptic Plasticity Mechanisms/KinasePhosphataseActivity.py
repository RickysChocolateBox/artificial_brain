import numpy as np

class KinasePhosphataseActivity:
    def __init__(self, modulation_rate, modulation_threshold, noise_std_dev):
        self.modulation_rate = modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update kinase/phosphatase activity
    def update_activity(self, activity_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update activity state based on activity level
        if activity_level >= self.modulation_threshold:
            activity_state += self.modulation_rate
        else:
            activity_state -= self.modulation_rate

        return activity_state

#This class represents the mechanism of modulation of kinase/phosphatase activity. The primary function, update_activity, updates the kinase/phosphatase activity state based on the activity level and random noise. The activity state is increased or decreased according to the modulation_rate depending on whether the activity level is above or below the modulation_threshold. 