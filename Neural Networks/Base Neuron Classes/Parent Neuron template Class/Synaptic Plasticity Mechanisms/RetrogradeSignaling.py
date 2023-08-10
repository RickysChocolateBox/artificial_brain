import numpy as np

class RetrogradeSignaling:
    def __init__(self, signaling_change_rate, signaling_threshold, noise_std_dev):
        self.signaling_change_rate = signaling_change_rate
        self.signaling_threshold = signaling_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update retrograde signaling based on activity level and noise
    def update_retrograde_signaling(self, signaling_strength, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update retrograde signaling based on activity level
        if activity_level >= self.signaling_threshold:
            signaling_strength += self.signaling_change_rate
        else:
            signaling_strength -= self.signaling_change_rate

        return signaling_strength

