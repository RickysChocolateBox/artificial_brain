import random
from AutoTuneToolkit import AutoTuneToolkit

class MedialSeptumNeuron:
    def __init__(self, id):
        self.id = id
        self.membrane_potential = -70.0
        self.resting_potential = -70.0
        self.threshold_potential = -55.0
        self.refractory_period = 2.0
        self.refractory_timer = 0.0
        self.local_inhibitory_connections = []
        self.local_excitatory_connections = []
        self.axon_hillock_length = random.uniform(5, 20)
        self.axon_initial_segment_length = random.uniform(10, 50)
        self.myelination = random.choice([True, False])
        self.myelin_sheath_thickness = random.uniform(0.1, 2) if self.myelination else 0
        self.astrocyte_interactions = random.randint(1, 10)
        self.intracellular_signaling_pathways = []
        self.ion_channels = {
            'leak': {'g': 0.05, 'E': -70.0},
            'Na': {'g': 120.0, 'E': 50.0},
            'K': {'g': 36.0, 'E': -77.0},
            'Ca': {'g': 1.0, 'E': 100.0},
            'HCN': {'g': 0.8, 'E': -20.0},  # Hyperpolarization-activated cyclic nucleotide-gated channel
        }

        self.neurotransmitter_release_probability = 0.5
        self.neurotransmitter_receptors = []
        self.axonal_arborization = []
        self.dendritic_spines = []

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
        self.cholinergic_neurons = False
        self.gabaergic_neurons = False
        self.glutamatergic_neurons = False
        self.neuropeptide_orexin = random.uniform(0, 1)
        self.neuropeptide_mch = random.uniform(0, 1)
        self.neuropeptide_cck = random.uniform(0, 1)
        self.relay_to_hippocampus = False
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

    def enable_cholinergic_neurons(self):
        self.cholinergic_neurons = True

    def disable_cholinergic_neurons(self):
        self.cholinergic_neurons = False

    def enable_gabaergic_neurons(self):
        self.gabaergic_neurons = True

    def disable_gabaergic_neurons(self):
        self.gabaergic_neurons = False

    def enable_glutamatergic_neurons(self):
        self.glutamatergic_neurons = True

    def disable_glutamatergic_neurons(self):
        self.glutamatergic_neurons = False

    def relay_to_hippocampus(self, target_neuron):
        self.relay_to_hippocampus = True

    def project_to_hippocampus(self, target_neurons):
        for neuron in target_neurons:
            neuron.receive_input_from_medial_septum(self.id)

    def project_to_entorhinal_cortex(self, target_neurons):
        for neuron in target_neurons:
            neuron.receive_input_from_medial_septum(self.id)

    def project_to_preoptic_area(self, target_neurons):
        for neuron in target_neurons:
            neuron.receive_input_from_medial_septum(self.id)

    def project_to_hypothalamus(self, target_neurons):
        for neuron in target_neurons:
            neuron.receive_input_from_medial_septum(self.id)

    def receive_input_from_lateral_septum(self, source_neuron_id):
        self.membrane_potential += 2

    def receive_input_from_amygdala(self, source_neuron_id):
        self.membrane_potential += 2

    def receive_input_from_entorhinal_cortex(self, source_neuron_id):
        self.membrane_potential += 2

    def synaptic_potentiation(self):
        self.synaptic_strength += 0.1

    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        self.integrate_post_synaptic_potentials()
        self.process_neuromodulation()
        self.fire_if_required()

        self.autotune_toolkit.optimize_neuron(self)