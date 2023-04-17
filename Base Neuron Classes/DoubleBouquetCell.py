import random
import numpy as np

class Neuron:
    def __init__(self, neuron_id):
        self.neuron_id = neuron_id
        self.connections = []

    def connect(self, other_neuron):
        self.connections.append(other_neuron)

class DoubleBouquetCell(Neuron):
    def __init__(self, neuron_id, axon_length, dendritic_branching_factor):
        super().__init__(neuron_id)
        self.neuron_type = "Double Bouquet cell"
        self.axon_length = axon_length
        self.dendritic_branching_factor = dendritic_branching_factor
        self.inhibitory_neurotransmitter = "GABA"

    def axon_branching(self):
        branches = random.randint(1, 5)
        return branches

    def dendritic_branching(self):
        dendritic_branches = self.dendritic_branching_factor * self.axon_length
        return dendritic_branches

    def process_input(self, input_data):
        processed_data = np.tanh(input_data)
        return processed_data

    def generate_output(self, input_data):
        threshold = 0.7
        output = (input_data > threshold).astype(int)
        return output

    def vertical_inhibition(self, input_data, inhibition_factor=0.4):
        inhibited_data = input_data * inhibition_factor
        return inhibited_data

    def release_neurotransmitter(self, output):
        if output:
            return self.inhibitory_neurotransmitter
        else:
            return None

