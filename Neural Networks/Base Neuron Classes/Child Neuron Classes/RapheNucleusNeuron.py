from AutoTuneToolkit import AutoTuneToolkit

class Neuron:
    def __init__(self, neuron_id):
        self.neuron_id = neuron_id
        self.connections = []


class RapheNucleusNeuron(Neuron):
    def __init__(self, neuron_id, serotonergic, modulation_rate, firing_threshold, axon_length, dendritic_tree, synaptic_delay, refractory_period):
        super().__init__(neuron_id)
        self.serotonergic = serotonergic
        self.modulation_rate = modulation_rate
        self.firing_threshold = firing_threshold
        self.axon_length = axon_length
        self.dendritic_tree = dendritic_tree
        self.synaptic_delay = synaptic_delay
        self.refractory_period = refractory_period
        self.tuning_toolkit = AutoTuneToolkit()
        self.received_inputs = []
        self.synaptic_weights = {}
        self.last_spike_time = None
        self.serotonin_receptors = []
        self.neurotransmitter_pool = {"serotonin": 0}

    def process_input(self, input_data, current_time):
        self.received_inputs.append(input_data)
        output_data = super().process_input(input_data)

        if self.serotonergic:
            modulated_input = self.modulate_input(input_data)
            output_data = self.compute_output(modulated_input, current_time)

        return output_data

    def modulate_input(self, input_data):
        return input_data * self.modulation_rate

    def compute_output(self, modulated_input, current_time):
        if self.last_spike_time is not None and current_time - self.last_spike_time < self.refractory_period:
            return 0

        if modulated_input > self.firing_threshold:
            self.last_spike_time = current_time
            self.release_neurotransmitter("serotonin")
            return 1
        else:
            return 0

    def tune_neuron(self, input_data):
        self.tuning_toolkit.tune_neuron(self, input_data)

    def update_synaptic_weights(self, synapse_id, new_weight):
        self.synaptic_weights[synapse_id] = new_weight

    def receive_serotonin(self, serotonin_level):
        self.modulation_rate = self.tuning_toolkit.adjust_modulation_rate(self.modulation_rate, serotonin_level)

    def propagate_signal(self, target_neuron, synapse_id):
        synaptic_weight = self.synaptic_weights[synapse_id]
        target_neuron.receive_signal(self.compute_output() * synaptic_weight, self.synaptic_delay)

    def release_neurotransmitter(self, neurotransmitter_type):
        if neurotransmitter_type in self.neurotransmitter_pool:
            self.neurotransmitter_pool[neurotransmitter_type] -= 1

    def replenish_neurotransmitter(self, neurotransmitter_type, amount):
        if neurotransmitter_type in self.neurotransmitter_pool:
            self.neurotransmitter_pool[neurotransmitter_type] += amount

