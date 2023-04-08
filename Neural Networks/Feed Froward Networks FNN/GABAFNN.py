import numpy as np
class GABAFNN:
    def __init__(self, inhibition_factor):
        self.inhibition_factor = inhibition_factor

    def weaken_connections(self, weights):
        absolute_weights = np.abs(weights)
        max_weight = np.max(absolute_weights)
        inhibition_threshold = max_weight * self.inhibition_factor
        inhibited_weights = np.where(absolute_weights > inhibition_threshold, weights, 0)
        return inhibited_weights
