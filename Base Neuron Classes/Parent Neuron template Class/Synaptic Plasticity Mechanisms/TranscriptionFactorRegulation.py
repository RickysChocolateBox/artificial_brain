import numpy as np

class TranscriptionFactorRegulation:
    def __init__(self, regulation_change_rate, regulation_threshold, noise_std_dev):
        self.regulation_change_rate = regulation_change_rate
        self.regulation_threshold = regulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update transcription factor regulation based on activity level and noise
    def update_regulation(self, regulation_strength, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update transcription factor regulation based on activity level
        if activity_level >= self.regulation_threshold:
            regulation_strength += self.regulation_change_rate
        else:
            regulation_strength -= self.regulation_change_rate

        return regulation_strength

