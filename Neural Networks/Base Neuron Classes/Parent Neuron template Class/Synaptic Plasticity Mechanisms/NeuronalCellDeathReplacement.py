import numpy as np

class NeuronalCellDeathReplacement:
    def __init__(self, death_threshold, replacement_rate, noise_std_dev):
        self.death_threshold = death_threshold
        self.replacement_rate = replacement_rate
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Check if a neuron should die and be replaced based on activity level and noise
    def check_cell_death_replacement(self, neuron_status, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # If activity level is below the death threshold, mark the neuron for replacement
        if activity_level <= self.death_threshold:
            neuron_status = 'replace'

        return neuron_status, activity_level

