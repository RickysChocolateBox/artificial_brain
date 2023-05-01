import numpy as np

class SynapticCleftProteins:
    def __init__(self, modulation_rate, modulation_threshold, noise_std_dev):
        self.modulation_rate = modulation_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update synaptic cleft proteins based on activity level and noise
    def update_synaptic_cleft_proteins(self, protein_modulation, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update synaptic cleft protein modulation based on activity level
        if activity_level >= self.modulation_threshold:
            protein_modulation += self.modulation_rate
        else:
            protein_modulation -= self.modulation_rate

        return protein_modulation

