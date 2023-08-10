import numpy as np

class PerineuronalNetPlasticity:
    def __init__(self, pnn_modulation_rate, modulation_threshold, noise_std_dev):
        self.pnn_modulation_rate = pnn_modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update perineuronal net plasticity based on activity level and noise
    def update_pnn(self, pnn_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update perineuronal net state based on activity level
        if activity_level >= self.modulation_threshold:
            pnn_state += self.pnn_modulation_rate
        else:
            pnn_state -= self.pnn_modulation_rate

        return pnn_state

