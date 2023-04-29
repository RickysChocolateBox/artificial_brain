import numpy as np
from scipy.signal import convolve2d
from AutoTuneToolkit import AutoTuneToolkit

class Neuron:
    def __init__(self, neuron_id):
        self.neuron_id = neuron_id
        self.connections = []

class AmacrineCell(Neuron):
    def __init__(self, neuron_id, axon_length, dendritic_branching_factor, neurotransmitter_pool):
        super().__init__(neuron_id)
        self.neuron_type = "Amacrine cell"
        self.axon_length = axon_length
        self.dendritic_branching_factor = dendritic_branching_factor
        self.inhibitory_neurotransmitter = "GABA"
        self.neurotransmitter_pool = neurotransmitter_pool
        self.auto_tune_toolkit = AutoTuneToolkit()

    def axon_branching(self):
        branches = self.auto_tune_toolkit.auto_tune(np.random.randint(1, 5))
        return branches

    def dendritic_branching(self):
        dendritic_branches = self.auto_tune_toolkit.auto_tune(self.dendritic_branching_factor * self.axon_length)
        return dendritic_branches

    def process_input(self, input_data):
        processed_data = np.tanh(input_data)
        return processed_data

    def lateral_inhibition(self, input_data, inhibition_factor=0.6):
        inhibited_data = input_data * inhibition_factor
        return inhibited_data

    def generate_output(self, input_data):
        threshold = self.auto_tune_toolkit.auto_tune(0.4)
        output = (input_data > threshold).astype(int)
        return output

    def spatial_filter(self, input_data):
        filter_kernel = self.auto_tune_toolkit.auto_tune(np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]))
        filtered_data = convolve2d(input_data, filter_kernel, mode='same')
        return filtered_data

    def release_neurotransmitter(self, output):
        if output:
            neurotransmitter = self.inhibitory_neurotransmitter
            self.neurotransmitter_pool -= 1
            return neurotransmitter
        else:
            return None

    def interact_with_bipolar_cells(self, bipolar_cell_output):
        modified_output = self.lateral_inhibition(bipolar_cell_output)
        return modified_output

    def regenerate_neurotransmitter(self, regeneration_rate):
        self.neurotransmitter_pool += regeneration_rate
        self.neurotransmitter_pool = min(self.neurotransmitter_pool, 100)

