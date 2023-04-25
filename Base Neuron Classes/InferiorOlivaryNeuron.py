import random
from autotune_toolkit import AutoTuneToolkit

class InferiorOlivaryNeuron:
    def __init__(self, id, autotune_toolkit):
        self.id = id
        self.autotune_toolkit = autotune_toolkit
        self.membrane_potential = -70.0
        self.resting_potential = -70.0
        self.threshold_potential = -50.0
        self.refractory_period = 4.0
        self.refractory_timer = 0.0
        self.local_inhibitory_connections = []
        self.local_excitatory_connections = []
        self.gap_junction_connections = []
        self.synaptic_weights = {}

        self.ion_channels = {
            'leak': {'g': 0.05, 'E': -70.0},
            'Na': {'g': 120.0, 'E': 50.0},
            'K': {'g': 36.0, 'E': -77.0},
            'Ca': {'g': 1.0, 'E': 100.0},
            'HCN': {'g': 0.8, 'E': -20.0},
            'T_type_Ca': {'g': 3.0, 'E': 120.0},
        }

    def connect_inhibitory(self, target_neuron):
        self.local_inhibitory_connections.append(target_neuron)

    def connect_excitatory(self, target_neuron):
        self.local_excitatory_connections.append(target_neuron)
        self.synaptic_weights[target_neuron.id] = self.autotune_toolkit.initialize_synaptic_weight()

    def update_ion_channels(self):
        for channel, properties in self.ion_channels.items():
            properties['g'] = self.autotune_toolkit.update_value(properties['g'])

    def release_inhibitory_neurotransmitter(self):
        for target_neuron in self.local_inhibitory_connections:
            target_neuron.receive_inhibition(self.id)

    def release_excitatory_neurotransmitter(self):
        for target_neuron in self.local_excitatory_connections:
            target_neuron.receive_excitation(self.id, self.synaptic_weights[target_neuron.id])

    def receive_inhibition(self, source_neuron_id):
        self.membrane_potential -= 2

    def receive_excitation(self, source_neuron_id, synaptic_weight):
        self.membrane_potential += synaptic_weight

    def fire_if_required(self, source_neuron_id):
        if self.membrane_potential >= self.threshold_potential:
            self.release_inhibitory_neurotransmitter()
            self.release_excitatory_neurotransmitter()
            self.membrane_potential = self.resting_potential
            self.enter_refractory_period()
        else:
            self.update_ion_channels()
            self.update_synaptic_weights(source_neuron_id)

    def enter_refractory_period(self):
        self.membrane_potential = self.resting_potential
        self.refractory_timer = self.refractory_period
        self.update_ion_channels()

    def update_synaptic_weights(self, source_neuron_id):
        self.synaptic_weights[source_neuron_id] = self.autotune_toolkit.update_synaptic_weight(self.synaptic_weights[source_neuron_id])

    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        for source_neuron_id in range(len(self.local_excitatory_connections)):
            self.fire_if_required(source_neuron_id)
    def connect_gap_junction(self, target_neuron):
        self.gap_junction_connections.append(target_neuron)

    def gap_junction_coupling(self):
        for target_neuron in self.gap_junction_connections:
            coupling_coefficient = self.autotune_toolkit.get_gap_junction_coupling_coefficient()
            self.membrane_potential += coupling_coefficient * (target_neuron.membrane_potential - self.membrane_potential)

    def simulate_subthreshold_oscillation(self):
        oscillation_amplitude = self.autotune_toolkit.get_oscillation_amplitude()
        oscillation_frequency = self.autotune_toolkit.get_oscillation_frequency()
        self.membrane_potential += oscillation_amplitude * random.uniform(-1, 1) * oscillation_frequency

    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        self.simulate_subthreshold_oscillation()
        self.gap_junction_coupling()

        for source_neuron_id in range(len(self.local_excitatory_connections)):
            self.fire_if_required(source_neuron_id)
    def simulate_subthreshold_oscillation(self):
        oscillation_amplitude = self.autotune_toolkit.get_oscillation_amplitude()
        oscillation_frequency = self.autotune_toolkit.get_oscillation_frequency()
        self.membrane_potential += oscillation_amplitude * random.uniform(-1, 1) * oscillation_frequency
        self.ion_channels['HCN']['g'] *= random.uniform(0.95, 1.05)
        self.ion_channels['T_type_Ca']['g'] *= random.uniform(0.95, 1.05)