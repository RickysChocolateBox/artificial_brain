import numpy as np

class DendriticSpineFormation:
    def __init__(self, formation_rate, threshold, activation_function):
        self.formation_rate = formation_rate
        self.threshold = threshold
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

    def form_spines(self, spine_strengths, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        formation_factor = self.formation_rate * activity_level
        spine_strengths += formation_factor
        spine_strengths = np.clip(spine_strengths, 0, self.threshold)
        return spine_strengths

