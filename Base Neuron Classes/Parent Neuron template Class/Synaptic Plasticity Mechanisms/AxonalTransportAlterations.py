import numpy as np

class AxonalTransportAlterations:
    def __init__(self, num_channels, learning_rate, activation_function, transport_rate, threshold):
        self.num_channels = num_channels
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.transport_rate = transport_rate
        self.threshold = threshold
        self.channel_activity = np.random.rand(num_channels)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_axonal_transport(self, activity):
        # Add random noise to activity
        noise = np.random.normal(0, 0.1)
        activity += noise

        # Apply the specified activation function to the activity level
        activity = self.apply_activation_function(activity)

        # Update channel activity based on the learning rate, transport rate, and activity level
        delta_channel_activity = self.learning_rate * self.transport_rate * activity
        self.channel_activity += delta_channel_activity

        # Ensure that the channel activity remains within the specified threshold
        self.channel_activity = np.clip(self.channel_activity, 0, self.threshold)

        return self.channel_activity

    def get_channel_activity(self):
        return self.channel_activity

