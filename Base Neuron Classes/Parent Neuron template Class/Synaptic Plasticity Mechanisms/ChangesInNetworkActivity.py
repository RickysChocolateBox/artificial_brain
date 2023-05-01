import numpy as np

class ChangesInNetworkActivity:
    def __init__(self, learning_rate, network_activity_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.network_activity_threshold = network_activity_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the network activity effect based on activity level and noise
    def update_network_activity_effect(self, network_activity_effect, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update network activity effect based on activity level
        if activity_level >= self.network_activity_threshold:
            network_activity_effect += self.learning_rate * (1 - network_activity_effect)
        else:
            network_activity_effect -= self.learning_rate * network_activity_effect

        return network_activity_effect

