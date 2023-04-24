import numpy as np
from AutoTuneToolkit import AutoTuneToolkit

class Neuron:
    def __init__(self, neuron_id):
        self.neuron_id = neuron_id
        self.connections = []

class ParvalbuminPositiveInterneuron(Neuron):
    def __init__(self, neuron_id, fast_spiking_property=True):
        super().__init__(neuron_id)
        self.neuron_type = "Parvalbumin-positive interneuron"
        self.inhibitory_neurotransmitter = "GABA"
        self.fast_spiking_property = fast_spiking_property
        self.auto_tune_toolkit = AutoTuneToolkit()
        self.morphology = "Basket cell" # PV+ interneurons often have basket cell morphology
        self.spatial_integration = "Local" # PV+ interneurons integrate inputs locally
        self.temporal_integration = "Fast" # PV+ interneurons exhibit fast temporal integration
        self.morphology = "Basket cell"
        

    def process_input(self, input_data):
        processed_data = np.tanh(input_data)
        return processed_data

    def apply_inhibition(self, input_data, inhibition_factor=0.5):
        inhibited_data = input_data * inhibition_factor
        return inhibited_data

    def generate_output(self, input_data):
        threshold = self.auto_tune_toolkit.auto_tune(0.5)
        output = (input_data > threshold).astype(int)
        return output

    def release_neurotransmitter(self, output):
        if output:
            neurotransmitter = self.inhibitory_neurotransmitter
            return neurotransmitter
        else:
            return None

    def fast_spiking(self, input_data):
        if self.fast_spiking_property:
            spike_rate = self.auto_tune_toolkit.auto_tune(1.5)
            input_data *= spike_rate
        return input_data

    def apply_temporal_integration(self, input_data):
        if self.temporal_integration == "Fast":
            integration_factor = self.auto_tune_toolkit.auto_tune(0.75)
            input_data *= integration_factor
        return input_data

    def apply_spatial_integration(self, input_data):
        if self.spatial_integration == "Local":
            spatial_factor = self.auto_tune_toolkit.auto_tune(0.5)
            input_data *= spatial_factor
        return input_data
    def apply_adaptation(self, input_data):
        if self.adaptation_property:
            adaptation_factor = self.auto_tune_toolkit.auto_tune(0.25)
            input_data *= (1 - adaptation_factor)
        return input_data

    def simulate_neuron(self, input_data):
        input_data = self.process_input(input_data)
        input_data = self.fast_spiking(input_data)
        input_data = self.apply_temporal_integration(input_data)
        input_data = self.apply_spatial_integration(input_data)
        input_data = self.apply_adaptation(input_data)
        output = self.generate_output(input_data)
        neurotransmitter = self.release_neurotransmitter(output)
        return neurotransmitter
