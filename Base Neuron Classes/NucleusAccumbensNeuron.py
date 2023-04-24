import random
from neuron_base import NeuronBase
from autotune_toolkit import AutoTuneToolkit

class NucleusAccumbensNeuron(NeuronBase):
    def __init__(self, neuron_id, firing_threshold, axon_length, dendritic_tree, synaptic_delay, refractory_period, dopamine_receptor_density, gaba_receptor_density, glutamate_receptor_density, calcium_concentration, potassium_concentration, membrane_potential, adaptation_rate):
        super().__init__(neuron_id)
        self.firing_threshold = firing_threshold
        self.axon_length = axon_length
        self.dendritic_tree = dendritic_tree
        self.synaptic_delay = synaptic_delay
        self.refractory_period = refractory_period
        self.dopamine_receptor_density = dopamine_receptor_density
        self.gaba_receptor_density = gaba_receptor_density
        self.glutamate_receptor_density = glutamate_receptor_density
        self.calcium_concentration = calcium_concentration
        self.potassium_concentration = potassium_concentration
        self.membrane_potential = membrane_potential
        self.tuning_toolkit = AutoTuneToolkit()
        self.received_inputs = []
        self.synaptic_weights = {}
        self.last_spike_time = None
        self.neurotransmitter_release_probability = 0.5
        self.neuronal_adaptation = 0
        self.adaptation_rate = adaptation_rate

    def process_input(self, input_data, neurotransmitter, current_time):
        self.received_inputs.append(input_data)
        output_data = super().process_input(input_data)

        modulated_input = self.apply_neurotransmitter_modulation(input_data, neurotransmitter)
        output_data = self.compute_output(modulated_input, current_time)

        return output_data

    def apply_neurotransmitter_modulation(self, input_data, neurotransmitter):
        if neurotransmitter == 'dopamine':
            return input_data * self.dopamine_receptor_density
        elif neurotransmitter == 'GABA':
            return input_data * self.gaba_receptor_density
        elif neurotransmitter == 'glutamate':
            return input_data * self.glutamate_receptor_density
        else:
            return input_data

    def compute_output(self, modulated_input, current_time):
        if self.last_spike_time is not None and current_time - self.last_spike_time < self.refractory_period:
            return 0

        self.neuronal_adaptation += self.adaptation_rate * (modulated_input - self.neuronal_adaptation)

        if modulated_input - self.neuronal_adaptation > self.firing_threshold:
            self.last_spike_time = current_time
            return 1
        else:
            return 0

    def propagate_signal(self, target_neuron, synapse_id, neurotransmitter):
        synaptic_weight = self.synaptic_weights[synapse_id]
        if self.check_neurotransmitter_release(neurotransmitter):
            target_neuron.process_input(self.compute_output() * synaptic_weight, neurotransmitter, self.synaptic_delay)

    def check_neurotransmitter_release(self, neurotransmitter):
        release_probability = self.neurotransmitter_release_probability
        return random.random() < release_probability

    def regulate_ionic_concentration(self):
        self.calcium_concentration = self.tuning_toolkit.regulate_calcium_concentration(self.calcium_concentration)
        self.potassium_concentration = self.tuning_toolkit.regulate
        self.potassium_concentration = self.tuning_toolkit.regulate_potassium_concentration(self.potassium_concentration)

    def update_membrane_potential(self, input_data):
        self.membrane_potential += input_data

    def update_synaptic_weights(self, learning_rate, target_neuron_id):
        if target_neuron_id not in self.synaptic_weights:
            self.synaptic_weights[target_neuron_id] = random.random()

        weight_change = learning_rate * (self.received_inputs[-1] - self.synaptic_weights[target_neuron_id])
        self.synaptic_weights[target_neuron_id] += weight_change

