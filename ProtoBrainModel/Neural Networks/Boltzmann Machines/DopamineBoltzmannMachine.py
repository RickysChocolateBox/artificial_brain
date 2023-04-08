import numpy as np

class Dopamine:
    def __init__(self, neurons):
        self.neurons = neurons
        self.weights = np.random.rand(neurons, neurons)
        
    def simulate(self, input_data, learning_rate):
        output = np.zeros(self.neurons)
        for i in range(self.neurons):
            activation = np.dot(self.weights[i], input_data)
            output[i] = 1 / (1 + np.exp(-activation))
        
        dopamine_level = np.mean(output)
        self.weights += learning_rate * dopamine_level * np.outer(output, output - np.mean(output))
        return output
