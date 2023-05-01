import numpy as np

class AxonalBoutonPlasticity:
    def __init__(self, bouton_modulation_rate, modulation_threshold, noise_std_dev):
        self.bouton_modulation_rate = bouton_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update axonal bouton plasticity based on activity level and noise
    def update_bouton(self, bouton_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update axonal bouton state based on activity level
        if activity_level >= self.modulation_threshold:
            bouton_state += self.bouton_modulation_rate
        else:
            bouton_state -= self.bouton_modulation_rate

        return bouton_state

