import numpy as np

class GABAergicTransmissionChanges:
    def __init__(self, gaba_rate, learning_rate, activation_function, threshold):
        self.gaba_rate = gaba_rate
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

    def update_gaba_transmission(self, gaba_transmission, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in GABAergic transmission based on the GABA rate and activity level
        change_in_gaba_transmission = self.gaba_rate * activity_level

        # Update the GABAergic transmission based on the learning rate and change in GABAergic transmission
        gaba_transmission += self.learning_rate * change_in_gaba_transmission

        # Ensure that the GABAergic transmission remains within the specified threshold
        gaba_transmission = np.clip(gaba_transmission, -self.threshold, self.threshold)

        return gaba_transmission

