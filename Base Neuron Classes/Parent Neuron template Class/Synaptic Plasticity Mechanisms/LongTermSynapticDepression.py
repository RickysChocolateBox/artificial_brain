import numpy as np

class LongTermSynapticDepression:
    def __init__(self, depression_rate, modulation_threshold, noise_std_dev):
        self.depression_rate = depression_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the synaptic strength based on activity level and random noise
    def update_depression(self, synaptic_strength, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Decrease synaptic strength based on activity level
        if activity_level < self.modulation_threshold:
            synaptic_strength -= self.depression_rate

        return synaptic_strength
# This class represents the mechanism of long-term synaptic depression. The primary function, update_depression, updates the synaptic strength based on the activity level and random noise. The synaptic strength is decreased according to the depression_rate if the activity level is below the modulation_threshold. The sigmoid function is used as the activation function.