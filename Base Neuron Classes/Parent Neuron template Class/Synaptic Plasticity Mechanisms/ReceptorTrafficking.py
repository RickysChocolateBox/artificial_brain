import numpy as np

class ReceptorTrafficking:
    def __init__(self, learning_rate, trafficking_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.trafficking_threshold = trafficking_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the receptor density based on activity level and noise
    def update_receptor_density(self, receptor_density, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update receptor density based on activity level
        if activity_level >= self.trafficking_threshold:
            receptor_density += self.learning_rate * (1 - receptor_density)
        else:
            receptor_density -= self.learning_rate * receptor_density

        return receptor_density

