import numpy as np
import tensorflow as tf
class GABAVAE:
    def __init__(self, threshold):
        self.threshold = threshold
        
    def inhibit_connections(self, weights):
        weights[weights > self.threshold] = 0
        return weights
