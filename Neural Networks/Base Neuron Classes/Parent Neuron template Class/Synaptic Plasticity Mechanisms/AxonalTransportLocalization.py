import numpy as np

class AxonalTransportLocalization:
    def __init__(self, learning_rate, transport_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.transport_threshold = transport_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the axonal transport rate based on activity level and noise
    def update_axonal_transport_rate(self, transport_rate, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update transport rate based on activity level
        if activity_level >= self.transport_threshold:
            transport_rate += self.learning_rate * (1 - transport_rate)
        else:
            transport_rate -= self.learning_rate * transport_rate

        return transport_rate

