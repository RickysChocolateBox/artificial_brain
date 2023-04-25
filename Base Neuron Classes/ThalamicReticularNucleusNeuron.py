import random
from AutoTuneToolkit import AutoTuneToolkit

class ThalamicReticularNucleusNeuron:
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
            'Ca_T': {'g': 1.0, 'E': 100.0},  # T-type calcium channel
            'Ca_L': {'g': 1.0, 'E': 100.0},  # L-type calcium channel
            'K_Ca': {'g': 1.0, 'E': -90.0},  # Calcium-activated potassium channel
        }

        self.neurotransmitter_release_probability = 0.5
        self.neurotransmitter_receptors = []
        self.axonal_arborization = []
        self.dendritic_spines = []
        self.burst_firing_mode = False
        self.tonic_firing_mode = True
        self.post_synaptic_potentials = []
        self.autotune_toolkit = AutoTuneToolkit(self)
        self.soma_diameter = random.uniform(15, 30)
        self.dendrite_diameter = random.uniform(1, 5)
        self.axon_diameter = random.uniform(1, 5)
        self.dendritic_tree_complexity = random.randint(3, 5)
        self.synaptic_vesicles = random.randint(100, 500)
        self.neurotransmitter_storage = random.uniform(0.1, 0.5)
        self.synaptic_cleft_width = random.uniform(20, 50)
        self.resting_calcium_concentration = random.uniform(0.05, 0.1)
        self.spike_frequency_adaptation = random.uniform(0.01, 0.1)
        self.spike_time_dependent_plasticity = random.uniform(0.01, 0.1)
        self.electrical_synapses = random.randint(1, 10)
        self.gap_junctions = random.randint(1, 10)
        self.synaptic_strength = random.uniform(0.1, 1.0)
        self.synaptic_delay = random.uniform(0.1, 1.0)
        self.glutamate_receptors = random.randint(10, 100)
        self.gaba_receptors = random.randint(10, 100)
        self.neurotransmitter_reuptake_rate = random.uniform(0.01, 0.1)
        self.synaptic_scaling = random.uniform(0.1, 1.0)
        self.homeostatic_plasticity = random.uniform(0.01, 0.1)
        self.neuromodulation = {}

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

    def enable_burst_firing_mode(self):
        self.burst_firing_mode = True

    def disable_burst_firing_mode(self):
        self.burst_firing_mode = False

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

        if self.burst_firing_mode:
            self.membrane_potential += random.uniform(-2, 2)

    def add_post_synaptic_potential(self, amplitude):
        self.post_synaptic_potentials.append(amplitude)

    def calculate_membrane_resistance(self):
        ion_channel_conductances = [properties['g'] for properties in self.ion_channels.values()]
        total_conductance = sum(ion_channel_conductances)
        return 1 / total_conductance
    def release_neurotransmitter(self, amount):
        self.neurotransmitter_storage -= amount
        if self.neurotransmitter_storage < 0:
            self.neurotransmitter_storage = 0

    def adjust_synaptic_strength(self, change):
        self.synaptic_strength += change
        if self.synaptic_strength < 0:
            self.synaptic_strength = 0

    def adjust_synaptic_delay(self, change):
        self.synaptic_delay += change
        if self.synaptic_delay < 0:
            self.synaptic_delay = 0

    def activate_neuromodulator(self, modulator, effect):
        self.neuromodulation[modulator] = effect

    def deactivate_neuromodulator(self, modulator):
        if modulator in self.neuromodulation:
            del self.neuromodulation[modulator]

    def process_neuromodulation(self):
        for modulator, effect in self.neuromodulation.items():
            effect(self)

    def update_receptor_count(self, receptor_type, change):
        if receptor_type == "glutamate":
            self.glutamate_receptors += change
        elif receptor_type == "gaba":
            self.gaba_receptors += change

    def adjust_neurotransmitter_reuptake_rate(self, change):
        self.neurotransmitter_reuptake_rate += change
        if self.neurotransmitter_reuptake_rate < 0:
            self.neurotransmitter_reuptake_rate = 0

    def adjust_synaptic_scaling(self, change):
        self.synaptic_scaling += change
        if self.synaptic_scaling < 0:
            self.synaptic_scaling = 0

    def adjust_homeostatic_plasticity(self, change):
        self.homeostatic_plasticity += change
        if self.homeostatic_plasticity < 0:
            self.homeostatic_plasticity = 0

    # Modify the simulate_time_step method to include the new methods and attributes
    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        self.integrate_post_synaptic_potentials()
        self.process_neuromodulation()
        self.fire_if_required()

        for target_neuron in self.local_excitatory_connections:
            target_neuron.receive_excitation(self.id)

        if self.burst_firing_mode:
            self.membrane_potential += random.uniform(-2, 2)

        self.autotune_toolkit.optimize_neuron(self)
