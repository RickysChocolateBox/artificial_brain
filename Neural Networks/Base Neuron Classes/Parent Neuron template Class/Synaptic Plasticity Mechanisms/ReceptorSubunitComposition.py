import numpy as np

class ReceptorSubunitComposition:
    def __init__(self, composition_rate, composition_threshold, noise_std_dev):
        self.composition_rate = composition_rate
        self.composition_threshold = composition_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update receptor subunit composition
    def update_composition(self, composition_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update composition state based on activity level
        if activity_level >= self.composition_threshold:
            composition_state += self.composition_rate
        else:
            composition_state -= self.composition_rate

        return composition_state

# This class represents the mechanism of changes in receptor subunit composition. The primary function, update_composition, updates the receptor subunit composition state based on the activity level and random noise. The composition state is increased or decreased according to the composition_rate depending on whether the activity level is above or below the composition_threshold.