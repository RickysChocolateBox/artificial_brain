class DopamineHopfieldNetworks:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def stimulate(self, weights, outputs, input_data):
        difference = input_data - outputs
        weights += self.learning_rate * difference * difference.T
        return weights

