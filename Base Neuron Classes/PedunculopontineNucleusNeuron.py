from autotunetoolkit import AutoTuneToolkit
import random

class PedunculopontineNucleusNeuron:
    def __init__(self, id):
        self.id = id
        self.membrane_potential = -70.0
        self.resting_potential = -70.0
        self.threshold_potential = -55.0
        self.refractory_period = 2.0
        self.refractory_timer = 0.0
        self.local_inhibitory_connections = []
        self.local_excitatory_connections = []

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
        self.pacemaker_activity = False
        self.post_synaptic_potentials = []
        self.autotune_toolkit = AutoTuneToolkit()
        self.soma_diameter = random.uniform(15, 30)
        self.dendrite_diameter = random.uniform(1, 5)
        self.axon_diameter = random.uniform(1, 5)
        self.dendritic_tree_complexity = random.randint(3, 5)

    def connect_inhibitory(self, target_neuron):
        self.local_inhibitory_connections.append(target_neuron)

    def connect_excitatory(self, target_neuron):
        self.local_excitatory_connections.append(target_neuron)

    def update_ion_channels(self):
        for channel, properties in self.ion_channels.items():
            properties['g'] *= random.uniform(0.95, 1.05)

    def release_inhibitory_neurotransmitter(self):
        for target_neuron in self.local_inhibitory_connections:
            target_neuron.receive_inhibition(self.id)

    def release_excitatory_neurotransmitter(self):
        for target_neuron in self.local_excitatory_connections:
            target_neuron.receive_excitation(self.id)

    def receive_inhibition(self, source_neuron_id):
        self.membrane_potential -= 2

    def receive_excitation(self, source_neuron_id):
        self.membrane_potential += 2

    def fire_if_required(self):
        if self.membrane_potential >= self.threshold_potential:
            self.release_inhibitory_neurotransmitter()
            self.release_excitatory_neurotransmitter()
            self.membrane_potential = self.resting_potential
            self.enter_refractory_period()
        else:
            self.update_ion_channels()

    def enter_refractory_period(self):
        self.membrane_potential = self.resting_potential
        self.refractory_timer = self.refractory_period
        self.update_ion_channels()

    def enable_pacemaker_activity(self):
        self.pacemaker_activity = True

    def disable_pacemaker_activity(self):
        self.pacemaker_activity = False

    def integrate_post_synaptic_potentials(self):
        self.membrane_potential += sum(self.post_synaptic_potentials)
        self.post_synaptic_potentials = []
    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        self.integrate_post_synaptic_potentials()
        self.fire_if_required()

        for target_neuron in self.local_excitatory_connections:
            target_neuron.receive_excitation(self.id)

        if self.pacemaker_activity:
            self.membrane_potential += random.uniform(-2, 2)

        self.autotune_toolkit.optimize_neuron(self)
        
    def add_post_synaptic_potential(self, amplitude):
        self.post_synaptic_potentials.append(amplitude)
        
    def calculate_membrane_resistance(self):
        ion_channel_conductances = [properties['g'] for properties in self.ion_channels.values()]
        total_conductance = sum(ion_channel_conductances)
        return 1 / total_conductance
    