import numpy as np

class DropoutRegularization:
    def __init__(self, dropout_prob):
        self.dropout_prob = dropout_prob

    def apply(self, layer):
        if self.dropout_prob > 0:
            layer_output = layer.output
            layer.dropout_mask = np.random.binomial(1, 1 - self.dropout_prob, size=layer_output.shape) / (1 - self.dropout_prob)
            layer.output *= layer.dropout_mask
        return layer

