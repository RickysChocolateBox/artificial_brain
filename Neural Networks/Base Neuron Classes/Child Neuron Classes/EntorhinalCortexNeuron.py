import numpy as np
from AutoTuneToolkit import AutoTuneToolkit

class EntorhinalCortexNeuron:
    def __init__(self, neuron_id, auto_tune_toolkit):
        self.neuron_id = neuron_id
        self.auto_tune_toolkit = auto_tune_toolkit
        self.voltage = -70.0
        self.calcium_concentration = 0.0
        self.synaptic_inputs = []
        self.synaptic_outputs = []
        self.synaptic_weights = {}
        self.threshold = -55.0
        self.resting_potential = -70.0
        self.refractory_period = 2.0
        self.time_since_last_spike = float('inf')
        self.current_time = 0.0
        self.dendritic_compartments = []
        self.axonal_compartments = []
        self.soma_size = None
        self.dendritic_length = None
        self.axonal_length = None
        self.ion_channels = {'NaV': {}, 'KV': {}, 'CaV': {}}
        self.receptor_subtypes = {'AMPA': {}, 'NMDA': {}, 'GABA_A': {}, 'GABA_B': {}}
        self.gene_expression = {}
        self.neuromodulator_concentrations = {}
        self.metabolic_processes = {}

    def update(self, delta_t):
        self.current_time += delta_t
        self.update_voltage(delta_t)
        self.update_calcium_concentration(delta_t)
        self.update_synaptic_weights()
        self.update_energy_balance(delta_t)
        self.modulate_by_neuromodulators(self.neuromodulator_concentrations)
        
        if self.voltage >= self.threshold and self.time_since_last_spike >= self.refractory_period:
            self.generate_action_potential()
            self.time_since_last_spike = 0
        else:
            self.time_since_last_spike += delta_t

    def update_energy_balance(self, delta_t):
        energy_consumption_rate = self.auto_tune_toolkit.get_parameter('energy_consumption_rate')
        energy_production_rate = self.auto_tune_toolkit.get_parameter('energy_production_rate')
        self.energy_balance += (energy_production_rate - energy_consumption_rate * self.calculate_energy_usage()) * delta_t

    def calculate_energy_usage(self):
        voltage_factor_weight = self.auto_tune_toolkit.get_parameter('voltage_factor_weight')
        calcium_factor_weight = self.auto_tune_toolkit.get_parameter('calcium_factor_weight')
        synaptic_activity_factor_weight = self.auto_tune_toolkit.get_parameter('synaptic_activity_factor_weight')

        voltage_factor = abs(self.voltage - self.resting_potential) / abs(self.threshold - self.resting_potential)
        calcium_factor = self.calcium_concentration / (self.calcium_concentration + 1.0)
        synaptic_activity_factor = sum([abs(weight) for weight in self.synaptic_weights.values()]) / len(self.synaptic_weights)

        energy_usage = (voltage_factor_weight * voltage_factor
                        + calcium_factor_weight * calcium_factor
                        + synaptic_activity_factor_weight * synaptic_activity_factor)
        return energy_usage

    def update_calcium_concentration(self, delta_t, activity):
        decay_rate = self.autotune_toolkit.get_parameter('decay_rate')
        self.Ca_concentration += activity * delta_t - self.Ca_concentration * decay_rate * delta_t

    def update_synaptic_weights(self, activity, target_neuron):
        learning_rate = self.autotune_toolkit.get_parameter('learning_rate')
        self.synaptic_weights[target_neuron] += learning_rate * activity

    def generate_action_potential(self):
        threshold = self.autotune_toolkit.get_parameter('threshold')
        if self.voltage >= threshold:
            self.spike_history.append(1)
            self.voltage = self.autotune_toolkit.get_parameter('v_reset')
        else:
            self.spike_history.append(0)

    def propagate_action_potential(self, connected_neurons):
        for neuron in connected_neurons:
            neuron.receive_spike(self.synaptic_weights[neuron])

    def receive_spike(self, synaptic_weight):
        self.voltage += synaptic_weight

    def modulate_by_neuromodulators(self, neuromodulator_concentrations):
        for neuromodulator, concentration in neuromodulator_concentrations.items():
            if neuromodulator == "dopamine":
                modulation_factor = self.autotune_toolkit.get_parameter('dopamine_modulation_factor')
                self.synaptic_weights = {neuron: weight * (1 + modulation_factor * concentration) for neuron, weight in self.synaptic_weights.items()}

    def process_sensory_input(self, sensory_input):
        sensory_weight = self.autotune_toolkit.get_parameter('sensory_weight')
        self.voltage += sensory_input * sensory_weight
