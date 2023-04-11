import numpy as np
class SerotoninANN:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.weights = None
        self.bias = None
    
    def train(self, input_data, output_data, epochs):
        # Initialize weights and bias randomly
        self.weights = np.random.rand(input_data.shape[1], output_data.shape[1])
        self.bias = np.random.rand(output_data.shape[1])

        for epoch in range(epochs):
            # Forward pass
            output = np.dot(input_data, self.weights) + self.bias

            # Backward pass
            error = output_data - output
            delta = error * self.learning_rate
            self.weights += np.dot(input_data.T, delta)
            self.bias += np.sum(delta, axis=0)
            
            # Simulate serotonin's role in balancing excitation and inhibition
            self.weights *= np.exp(-np.abs(delta))
            self.bias *= np.exp(-np.abs(delta))
            
    def predict(self, input_data):
        output = np.dot(input_data, self.weights) + self.bias
        return output

