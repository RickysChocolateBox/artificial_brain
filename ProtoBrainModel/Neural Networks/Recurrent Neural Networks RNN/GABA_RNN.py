import numpy as np

class GABANNANN:
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size)
        
    def inhibit_connections(self, threshold):
        self.weights[self.weights > threshold] = 0
        
    def activate(self, input_data):
        output = np.dot(input_data, self.weights)
        return output
