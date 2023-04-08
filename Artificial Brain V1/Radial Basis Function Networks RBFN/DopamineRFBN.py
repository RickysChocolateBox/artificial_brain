import numpy as np

class DopamineRFBN:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
    
    def strengthen_connections(self, neurons, input_data):
        activation = np.sum(np.square(neurons - input_data), axis=1)
        winner = np.argmin(activation)
        neurons[winner] += self.learning_rate * (input_data - neurons[winner])
        return neurons

