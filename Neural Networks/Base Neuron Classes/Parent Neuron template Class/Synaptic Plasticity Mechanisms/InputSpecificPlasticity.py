import numpy as np

class InputSpecificPlasticity:
    def __init__(self, learning_rate, input_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.input_threshold = input_threshold
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_input_specific(self, synaptic_weight, input_level):
        noise = np.random.normal(0, self.noise_std_dev)
        input_level = self.sigmoid(input_level + noise)

        if input_level >= self.input_threshold:
            synaptic_weight += self.learning_rate * (1 - synaptic_weight)
        else:
            synaptic_weight -= self.learning_rate * synaptic_weight

        return synaptic_weight

