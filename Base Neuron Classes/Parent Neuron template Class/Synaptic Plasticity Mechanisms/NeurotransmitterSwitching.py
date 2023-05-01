import numpy as np

class NeurotransmitterSwitching:
    def __init__(self, learning_rate, switching_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.switching_threshold = switching_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the neurotransmitter switching probability based on activity level and noise
    def update_switching_probability(self, switching_probability, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update switching probability based on activity level
        if activity_level >= self.switching_threshold:
            switching_probability += self.learning_rate * (1 - switching_probability)
        else:
            switching_probability -= self.learning_rate * switching_probability

        return switching_probability

