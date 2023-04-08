import numpy as np
class GABARFBN:
    def __init__(self, connection_factor):
        self.connection_factor = connection_factor
    
    def weaken_connections(self, neurons, input_data):
        activation = np.sum(np.square(neurons - input_data), axis=1)
        connections = np.where(activation < self.connection_factor, 1, 0)
        neurons *= connections[:, np.newaxis]
        return neurons
