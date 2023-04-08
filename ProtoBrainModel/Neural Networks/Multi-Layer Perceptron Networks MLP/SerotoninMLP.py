import numpy as np
class SerotoninMLP:
    def __init__(self, num_layers, input_size, hidden_size, output_size):
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights = []
        self.serotonin = 0.5
        
        for i in range(num_layers - 1):
            self.weights.append(np.random.randn(hidden_size, hidden_size))
        self.weights.append(np.random.randn(hidden_size, output_size))
        
    def forward(self, x):
        h = np.zeros((self.num_layers, self.hidden_size))
        h[0] = x
        for i in range(1, self.num_layers):
            h[i] = np.maximum(0, np.dot(h[i-1], self.weights[i-1]) + self.serotonin)
        output = np.dot(h[self.num_layers - 1], self.weights[self.num_layers - 1])
        return output
    
    def update_serotonin(self, input_excitation, input_inhibition):
        self.serotonin = (input_excitation - input_inhibition) / 10

