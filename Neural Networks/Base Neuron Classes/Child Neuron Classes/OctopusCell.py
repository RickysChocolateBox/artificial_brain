import random
import numpy as np
from AutoTuneToolkit import AutoTuneToolkit

class Neuron:
    def __init__(self, neuron_id):
        self.neuron_id = neuron_id
        self.connections = []

    def connect(self, other_neuron, connection_strength):
        self.connections.append((other_neuron, connection_strength))

class OctopusCell(Neuron):
    def __init__(self, neuron_id, axon_length, dendritic_branching_factor):
        super().__init__(neuron_id)
        self.neuron_type = "Octopus cell"
        self.axon_length = axon_length
        self.dendritic_branching_factor = dendritic_branching_factor
        self.excitatory_neurotransmitter = "Glutamate"

    def axon_branching(self):
        branches = random.randint(1, 3)
        return branches

    def dendritic_branching(self):
        dendritic_branches = self.dendritic_branching_factor * self.axon_length
        return dendritic_branches

    def process_input(self, input_data):
        processed_data = np.tanh(input_data)
        return processed_data

    def generate_output(self, input_data):
        threshold = 0.6
        output = (input_data > threshold).astype(int)
        return output

    def release_neurotransmitter(self, output):
        if output:
            return self.excitatory_neurotransmitter
        else:
            return None

    def timing_detection(self, input_data, timing_threshold=0.01):
        time_diffs = np.diff(input_data)
        detected_timing = (time_diffs < timing_threshold).astype(int)
        return detected_timing

    def integrate_inputs(self, input_data_list):
        integrated_data = sum(input_data_list) / len(input_data_list)
        return integrated_data

    def sound_onset_processing(self, input_data, onset_threshold=0.5):
        onset_output = (input_data > onset_threshold).astype(int)
        return onset_output

    def interaural_time_difference_processing(self, left_ear_data, right_ear_data, max_itd=0.001):
        time_difference = np.abs(left_ear_data - right_ear_data)
        itd_output = (time_difference < max_itd).astype(int)
        return itd_output

