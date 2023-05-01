import numpy as np

class SilentSynapseFormation:
    def __init__(self, learning_rate, formation_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.formation_threshold = formation_threshold
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_silent_synapse(self, synapse_state, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        if activity_level >= self.formation_threshold:
            synapse_state = 1
        else:
            synapse_state = 0

        return synapse_state

