import numpy as np

class RegulationExcitatoryInhibitoryBalance:
    def __init__(self, balance_rate, learning_rate, activation_function, threshold):
        self.balance_rate = balance_rate
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

    def update_excitatory_inhibitory_balance(self, balance, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in balance based on the balance rate and activity level
        change_in_balance = self.balance_rate * activity_level

        # Update the balance based on the learning rate and change in balance
        balance += self.learning_rate * change_in_balance

        # Ensure that the balance remains within the specified threshold
        balance = np.clip(balance, -self.threshold, self.threshold)

        return balance

