import numpy as np

class AxonTerminalMorphologyChanges:
    def __init__(self, morphology_rate, learning_rate, activation_function, threshold):
        self.morphology_rate = morphology_rate
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

    def update_axon_terminal_morphology(self, axon_morphology, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_morphology = self.morphology_rate * activity_level
        axon_morphology += self.learning_rate * change_in_morphology
        axon_morphology = np.clip(axon_morphology, -self.threshold, self.threshold)
        return axon_morphology

