import numpy as np

class ModulationOfNeuronalDeathAndSurvival:
    def __init__(self, death_rate, survival_rate, learning_rate, activation_function):
        self.death_rate = death_rate
        self.survival_rate = survival_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_neuronal_status(self, neuronal_activity):
        # Apply the specified activation function to the neuronal activity
        activity = self.apply_activation_function(neuronal_activity)

        # Update neuronal death and survival probabilities based on the learning rate and activity level
        death_probability = self.learning_rate * self.death_rate * (1 - activity)
        survival_probability = self.learning_rate * self.survival_rate * activity

        return death_probability, survival_probability

