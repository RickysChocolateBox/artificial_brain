import numpy as np

class SynapticAugmentation:
    def __init__(self, augmentation_rate, threshold, activation_function):
        self.augmentation_rate = augmentation_rate
        self.threshold = threshold
        self.activation_function = activation_function

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def augment_synapses(self, synapse_strengths, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        augmentation_factor = self.augmentation_rate * activity_level
        synapse_strengths *= (1 + augmentation_factor)
        synapse_strengths = np.clip(synapse_strengths, 0, self.threshold)
        return synapse_strengths

