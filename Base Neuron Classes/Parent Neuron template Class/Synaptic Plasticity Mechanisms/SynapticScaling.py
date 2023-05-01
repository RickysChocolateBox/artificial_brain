import numpy as np

class SynapticScaling:
    def __init__(self, scaling_rate, scaling_threshold, noise_std_dev):
        self.scaling_rate = scaling_rate
        self.scaling_threshold = scaling_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update synaptic scaling of receptor expression
    def update_scaling(self, scaling_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update scaling state based on activity level
        if activity_level >= self.scaling_threshold:
            scaling_state += self.scaling_rate
        else:
            scaling_state -= self.scaling_rate

        return scaling_state

# This class represents the mechanism of synaptic scaling of receptor expression. The primary function, update_scaling, updates the synaptic scaling state based on the activity level and random noise. The scaling state is increased or decreased according to the scaling_rate depending on whether the activity level is above or below the scaling_threshold.