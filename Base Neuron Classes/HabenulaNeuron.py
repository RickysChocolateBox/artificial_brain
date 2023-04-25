from autotunetoolkit import AutoTuneToolkit
import random

class HabenulaNeuron:
    def __init__(self, id):
        self.id = id
        self.membrane_potential = -70.0
        self.resting_potential = -70.0
        self.threshold_potential = -55.0
        self.refractory_period = 2.0
        self.refractory_timer = 0.0
        self.local_connections = []

        self.ion_channels = {
            'leak': {'g': 0.05, 'E': -70.0},
            'Na': {'g': 120.0, 'E': 50.0},
            'K': {'g': 36.0, 'E': -77.0},
            'Ca': {'g': 1.0, 'E': 100.0},
        }

        self.neurotransmitter_release_probability = 0.5
        self.neurotransmitter_receptors = []
        self.axonal_arborization = []
        self.dendritic_spines = []
        self.plasticity_factor = 0.01

    def connect(self, target_neuron):
        self.local_connections.append(target_neuron)

    def update_ion_channels(self):
        for channel, properties in self.ion_channels.items():
            properties['g'] = AutoTuneToolkit.auto_tune_property(properties['g'], 0.95, 1.05)

    def release_neurotransmitter(self):
        if random.random() < self.neurotransmitter_release_probability:
            for receptor in self.neurotransmitter_receptors:
                receptor.receive_neurotransmitter()

    def modulate_activity(self, neurotransmitter_sensitivity):
        self.membrane_potential += neurotransmitter_sensitivity

    def fire_if_required(self):
        if self.membrane_potential >= self.threshold_potential:
            self.release_neurotransmitter()
            self.membrane_potential = self.resting_potential
            self.enter_refractory_period()
        else:
            self.update_ion_channels()

    def enter_refractory_period(self):
        self.membrane_potential = self.resting_potential
        self.refractory_timer = self.refractory_period
        self.update_ion_channels()

    def extend_axon(self, target_neuron):
        self.axonal_arborization.append(target_neuron)

    def add_dendritic_spine(self, dendrite):
        self.dendritic_spines.append(dendrite)

    def update_synaptic_weights(self, source_neuron_id):
        for connection in self.local_connections:
            connection.weight += self.plasticity_factor * (connection.target_neuron.membrane_potential - connection.source_neuron.membrane_potential)

    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        self.fire_if_required()

        for target_neuron in self.axonal_arborization:
            target_neuron.receive_excitation(self.id)

        self.update_synaptic_weights(self.id)