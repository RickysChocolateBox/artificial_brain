import numpy as np

class PostsynapticReceptorTrafficking:
    def __init__(self, trafficking_rate, learning_rate, activation_function, threshold):
        self.trafficking_rate = trafficking_rate
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

    def update_receptor_trafficking(self, receptor_density, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_density = self.trafficking_rate * activity_level
        receptor_density += self.learning_rate * change_in_density
        receptor_density = np.clip(receptor_density, -self.threshold, self.threshold)
        return receptor_density

