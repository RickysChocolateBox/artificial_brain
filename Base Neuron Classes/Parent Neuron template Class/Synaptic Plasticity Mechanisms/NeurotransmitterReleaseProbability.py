import numpy as np

class NeurotransmitterReleaseProbability:
    def __init__(self, learning_rate, release_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.release_threshold = release_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the release probability based on activity level and noise
    def update_release_probability(self, release_probability, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update release probability based on activity level
        if activity_level >= self.release_threshold:
            release_probability += self.learning_rate * (1 - release_probability)
        else:
            release_probability -= self.learning_rate * release_probability

        return release_probability

