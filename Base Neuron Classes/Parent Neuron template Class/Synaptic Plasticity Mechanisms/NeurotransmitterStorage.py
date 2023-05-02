import numpy as np

class NeurotransmitterStorage:
    def __init__(self, storage_capacity, storage_rate, activation_function='sigmoid'):
        self.storage_capacity = storage_capacity
        self.storage_rate = storage_rate
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

    def update_storage(self, neurotransmitter_amount, activity_levels):
        activity_levels = self.apply_activation_function(activity_levels)
        storage_change = self.storage_rate * activity_levels
        neurotransmitter_amount += storage_change
        neurotransmitter_amount = np.clip(neurotransmitter_amount, 0, self.storage_capacity)
        return neurotransmitter_amount

