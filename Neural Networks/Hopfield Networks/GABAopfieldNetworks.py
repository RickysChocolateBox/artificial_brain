class GABAopfieldNetworks:
    def __init__(self, threshold):
        self.threshold = threshold
        
    def control_activation(self, network):
        for neuron in network:
            if neuron.activation > self.threshold:
                neuron.activation = 0

