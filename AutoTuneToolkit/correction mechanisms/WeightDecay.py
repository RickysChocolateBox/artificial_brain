import numpy as np

class WeightDecay:
    def __init__(self, lambda_val):
        self.lambda_val = lambda_val
        
    def compute_gradient(self, weights):
        return self.lambda_val * weights
    
    def update_weights(self, weights, gradients, learning_rate):
        weights -= learning_rate * (gradients + self.compute_gradient(weights))

