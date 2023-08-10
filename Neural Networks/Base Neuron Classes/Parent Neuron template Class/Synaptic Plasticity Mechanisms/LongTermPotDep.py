import numpy as np

class LongTermPotDep:
    def __init__(self, potentiation_rate, depression_rate, potentiation_threshold, depression_threshold,
                 max_synaptic_strength, min_synaptic_strength, learning_rate, noise_std_dev):
        self.potentiation_rate = potentiation_rate
        self.depression_rate = depression_rate
        self.potentiation_threshold = potentiation_threshold
        self.depression_threshold = depression_threshold
        self.max_synaptic_strength = max_synaptic_strength
        self.min_synaptic_strength = min_synaptic_strength
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_synaptic_strength(self, synaptic_strength, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        if activity_level >= self.potentiation_threshold:
            synaptic_strength += self.learning_rate * self.potentiation_rate
        elif activity_level <= self.depression_threshold:
            synaptic_strength -= self.learning_rate * self.depression_rate

        synaptic_strength = np.clip(synaptic_strength, self.min_synaptic_strength, self.max_synaptic_strength)
        return synaptic_strength

