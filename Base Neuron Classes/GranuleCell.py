import random
import numpy as np
from AutoTuneToolkit import AutoTuneToolkit

class Neuron:
    def __init__(self, neuron_id):
        self.neuron_id = neuron_id
        self.connections = []

    def connect(self, other_neuron, connection_strength):
        self.connections.append((other_neuron, connection_strength))

class GranuleCell(Neuron):
    def __init__(self, neuron_id, dendritic_branching_factor):
        super().__init__(neuron_id)
        self.neuron_type = "Granule cell"
        self.dendritic_branching_factor = dendritic_branching_factor
        self.inhibitory_neurotransmitter = "GABA"

    def dendritic_branching(self):
        dendritic_branches = random.randint(2, 5) * self.dendritic_branching_factor
        return dendritic_branches

    def process_input(self, input_data):
        processed_data = np.tanh(input_data)
        return processed_data

    def generate_output(self, input_data):
        threshold = 0.5
        output = (input_data > threshold).astype(int)
        return output

    def release_neurotransmitter(self, output):
        if output:
            return self.inhibitory_neurotransmitter
        else:
            return None

    def synaptic_integration(self, input_data):
        synaptic_factor = AutoTuneToolkit.tune(input_data)
        return synaptic_factor

    def generate_morphology(self):
        morphology = {}
        branches = self.dendritic_branching()
        for i in range(branches):
            branch_length = random.uniform(0.1, 1)
            morphology[f'branch_{i+1}'] = branch_length
        return morphology

    def lateral_inhibition(self, input_data, inhibition_factor=0.6):
        inhibited_data = input_data * inhibition_factor
        return inhibited_data

    def synaptic_plasticity(self, connection_strength, plasticity_factor):
        new_strength = connection_strength * plasticity_factor
        return new_strength

    def neuromodulator_effect(self, neuromodulator, effect_strength):
        if neuromodulator == "dopamine":
            response_factor = 1 + effect_strength
        elif neuromodulator == "serotonin":
            response_factor = 1 - effect_strength
        else:
            response_factor = 1

        return response_factor

    def reciprocal_dendrodendritic_synapse(self, mitral_cell_input):
        inhibition_level = np.sum(mitral_cell_input) * -1
        return inhibition_level

    def glomerular_module_formation(self, mitral_cell_input, tufted_cell_input):
        combined_input = np.concatenate((mitral_cell_input, tufted_cell_input))
        module_input = np.mean(combined_input)
        return module_input

