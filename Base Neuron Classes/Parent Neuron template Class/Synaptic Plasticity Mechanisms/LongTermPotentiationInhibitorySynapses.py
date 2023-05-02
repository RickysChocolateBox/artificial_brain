import numpy as np

class LongTermPotentiationInhibitorySynapses:
    def __init__(self, ltp_rate, learning_rate, activation_function, threshold):
        self.ltp_rate = ltp_rate
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

    def update_ltp_inhibitory_synapses(self, synaptic_strength, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the long-term potentiation based on the LTP rate and activity level
        ltp = self.ltp_rate * activity_level

        # Update synaptic strength based on the learning rate and LTP
        synaptic_strength -= self.learning_rate * ltp

        # Ensure that the synaptic strength remains within the specified threshold
        synaptic_strength = np.clip(synaptic_strength, -self.threshold, 0)

        return synaptic_strength

