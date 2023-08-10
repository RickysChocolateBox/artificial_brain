import numpy as np

class GlialNeuronalInteractionsPlasticity:
    def __init__(self, learning_rate, glial_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.glial_threshold = glial_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the glial-neuronal interaction effect based on activity level and noise
    def update_glial_neuronal_interaction(self, interaction_effect, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update interaction effect based on activity level
        if activity_level >= self.glial_threshold:
            interaction_effect += self.learning_rate * (1 - interaction_effect)
        else:
            interaction_effect -= self.learning_rate * interaction_effect

        return interaction_effect

