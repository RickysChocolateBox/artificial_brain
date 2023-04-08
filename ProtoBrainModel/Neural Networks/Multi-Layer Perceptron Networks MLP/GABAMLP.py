import numpy as np

class GABAMLP:
    def __init__(self, strength):
        self.strength = strength
        
    def inhibit(self, connections):
        for i in range(len(connections)):
            for j in range(len(connections[i])):
                if np.abs(connections[i][j]) > self.strength:
                    connections[i][j] = 0.0
                else:
                    connections[i][j] *= 0.5
        return connections

