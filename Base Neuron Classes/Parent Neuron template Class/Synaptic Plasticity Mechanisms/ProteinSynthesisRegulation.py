import numpy as np

class ProteinSynthesisRegulation:
    def __init__(self, learning_rate, synthesis_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.synthesis_threshold = synthesis_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the protein synthesis rate based on activity level and noise
    def update_protein_synthesis_rate(self, synthesis_rate, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update synthesis rate based on activity level
        if activity_level >= self.synthesis_threshold:
            synthesis_rate += self.learning_rate * (1 - synthesis_rate)
        else:
            synthesis_rate -= self.learning_rate * synthesis_rate

        return synthesis_rate

