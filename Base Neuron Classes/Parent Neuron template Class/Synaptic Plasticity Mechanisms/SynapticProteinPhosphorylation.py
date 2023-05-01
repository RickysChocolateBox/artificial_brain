import numpy as np

class SynapticProteinPhosphorylation:
    def __init__(self, phosphorylation_rate, phosphorylation_threshold, noise_std_dev):
        self.phosphorylation_rate = phosphorylation_rate
        self.phosphorylation_threshold = phosphorylation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update synaptic protein phosphorylation
    def update_phosphorylation(self, phosphorylation_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update phosphorylation state based on activity level
        if activity_level >= self.phosphorylation_threshold:
            phosphorylation_state += self.phosphorylation_rate
        else:
            phosphorylation_state -= self.phosphorylation_rate

        return phosphorylation_state

#This class represents the mechanism of changes in synaptic protein phosphorylation. The primary function, update_phosphorylation, updates the synaptic protein phosphorylation state based on the activity level and random noise. The phosphorylation state is increased or decreased according to the phosphorylation_rate depending on whether the activity level is above or below the phosphorylation_threshold.