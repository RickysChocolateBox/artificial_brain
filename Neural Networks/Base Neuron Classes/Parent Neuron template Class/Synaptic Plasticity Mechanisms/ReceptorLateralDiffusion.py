import numpy as np

class ReceptorLateralDiffusion:
    def __init__(self, diffusion_rate, activation_function='sigmoid'):
        self.diffusion_rate = diffusion_rate
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

    def update_lateral_diffusion(self, receptor_distribution, activity_levels):
        activity_levels = self.apply_activation_function(activity_levels)
        receptor_diffusion = self.diffusion_rate * np.outer(activity_levels, activity_levels)
        receptor_distribution += receptor_diffusion
        return receptor_distribution

