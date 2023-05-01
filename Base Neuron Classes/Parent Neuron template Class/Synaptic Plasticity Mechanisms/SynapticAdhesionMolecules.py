import numpy as np

class SynapticAdhesionMolecules:
    def __init__(self, adhesion_change_rate, adhesion_threshold, noise_std_dev):
        self.adhesion_change_rate = adhesion_change_rate
        self.adhesion_threshold = adhesion_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update synaptic adhesion molecules based on activity level and noise
    def update_synaptic_adhesion_molecules(self, adhesion_level, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update synaptic adhesion level based on activity level
        if activity_level >= self.adhesion_threshold:
            adhesion_level += self.adhesion_change_rate
        else:
            adhesion_level -= self.adhesion_change_rate

        return adhesion_level

