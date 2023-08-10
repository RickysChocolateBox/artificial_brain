import numpy as np

class IonChannelExpressionModulation:
    def __init__(self, channel_modulation_rate, learning_rate, noise_std_dev):
        self.channel_modulation_rate = channel_modulation_rate
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_channel_expression(self, channel_expression, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        channel_expression += self.learning_rate * self.channel_modulation_rate * activity_level

        return channel_expression

