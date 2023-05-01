import numpy as np

class MyelinationDemyelination:
    def __init__(self, myelination_rate, demyelination_rate, myelination_threshold, demyelination_threshold, noise_std_dev):
        self.myelination_rate = myelination_rate
        self.demyelination_rate = demyelination_rate
        self.myelination_threshold = myelination_threshold
        self.demyelination_threshold = demyelination_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update myelination level based on activity level and noise
    def update_myelination(self, myelination_level, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update myelination level based on activity level
        if activity_level >= self.myelination_threshold:
            myelination_level += self.myelination_rate
        elif activity_level <= self.demyelination_threshold:
            myelination_level -= self.demyelination_rate

        return myelination_level

