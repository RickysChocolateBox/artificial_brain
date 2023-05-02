import numpy as np

class SynapticTransmissionChanges:
    def __init__(self, transmission_rate, learning_rate, activation_function, threshold):
        self.transmission_rate = transmission_rate
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

    def update_synaptic_transmission(self, synaptic_transmission, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate the change in synaptic transmission based on the transmission rate and activity level
        change_in_synaptic_transmission = self.transmission_rate * activity_level

        # Update the synaptic transmission based on the learning rate and change in synaptic transmission
        synaptic_transmission += self.learning_rate * change_in_synaptic_transmission

        # Ensure that the synaptic transmission remains within the specified threshold
        synaptic_transmission = np.clip(synaptic_transmission, -self.threshold, self.threshold)

        return synaptic_transmission

