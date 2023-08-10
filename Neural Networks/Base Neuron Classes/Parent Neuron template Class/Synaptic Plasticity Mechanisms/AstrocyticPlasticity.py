import numpy as np

class AstrocyticPlasticity:
    def __init__(self, astrocyte_modulation_rate, modulation_threshold, noise_std_dev):
        self.astrocyte_modulation_rate = astrocyte_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update astrocytic plasticity based on activity level and noise
    def update_astrocyte(self, astrocyte_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update astrocyte state based on activity level
        if activity_level >= self.modulation_threshold:
            astrocyte_state += self.astrocyte_modulation_rate
        else:
            astrocyte_state -= self.astrocyte_modulation_rate

        return astrocyte_state

