import numpy as np

class SpineMorphology:
    def __init__(self, morphology_modulation_rate, modulation_threshold, noise_std_dev):
        self.morphology_modulation_rate = morphology_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update spine morphology based on activity level and noise
    def update_morphology(self, morphology, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update morphology based on activity level
        if activity_level >= self.modulation_threshold:
            morphology += self.morphology_modulation_rate
        else:
            morphology -= self.morphology_modulation_rate

        return morphology

