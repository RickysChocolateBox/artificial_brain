import numpy as np

class NeuronalActivityDependentSynapticCompetition:
    def __init__(self, competition_rate, learning_rate, activation_function, threshold):
        self.competition_rate = competition_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.threshold = threshold

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_synaptic_competition(self, synaptic_strength, activity_level):
        # Apply the specified activation function to the activity level
        activity_level = self.apply_activation_function(activity_level)

        # Calculate synaptic competition based on the competition rate and activity level
        synaptic_competition = self.competition_rate * activity_level

        # Update synaptic strength based on the learning rate and synaptic competition
        synaptic_strength += self.learning_rate * synaptic_competition

        # Ensure that the synaptic strength remains within the specified threshold
        synaptic_strength = np.clip(synaptic_strength, -self.threshold, self.threshold)

        return synaptic_strength

