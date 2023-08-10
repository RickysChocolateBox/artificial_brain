import numpy as np

class VoltageGatedChannelExpressionChanges:
    def __init__(self, channel_rate, learning_rate, activation_function, threshold):
        self.channel_rate = channel_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.threshold = threshold

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_channel_expression(self, channel_expression, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in channel expression based on the channel rate and activity level
        change_in_channel_expression = self.channel_rate * activity_level

        # Update the channel expression based on the learning rate and change in channel expression
        channel_expression += self.learning_rate * change_in_channel_expression

        # Ensure that the channel expression remains within the specified threshold
        channel_expression = np.clip(channel_expression, -self.threshold, self.threshold)

        return channel_expression

