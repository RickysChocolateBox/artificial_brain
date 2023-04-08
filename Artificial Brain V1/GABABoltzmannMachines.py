import numpy as np

class GABABoltzmannMachines:
    def __init__(self, neurons):
        self.neurons = neurons
        self.inhibition_rate = 1.0
        
    def simulate(self, input_data):
        output = np.zeros(self.neurons)
        for i in range(self.neurons):
            activation = np.dot(self.weights[i], input_data)
            output[i] = 1 / (1 + np.exp(-activation)) - self.inhibition_rate / (1 + np.exp(activation))
        return output
    
    def update_inhibition_rate(self, rate):
        self.inhibition_rate = rate

