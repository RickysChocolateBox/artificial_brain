import random
from AutoTuneToolkit import AutoTuneToolkit

class SuprachiasmaticNucleusNeuron:
    def __init__(self, id):
        self.id = id
        self.membrane_potential = -70.0
        self.resting_potential = -70.0
        self.threshold_potential = -55.0
        self.refractory_period = 2.0
        self.refractory_timer = 0.0
        self.local_inhibitory_connections = []
        self.local_excitatory_connections = []
        self.post_synaptic_potentials = []
        self.neuropeptide_vip = random.uniform(0.1, 1.0)  # Vasoactive intestinal peptide
        self.neuropeptide_avp = random.uniform(0.1, 1.0)  # Arginine vasopressin
        self.neuropeptide_grpr = random.uniform(0.1, 1.0)  # Gastrin-releasing peptide receptor
        self.neuropeptide_ror = random.uniform(0.1, 1.0)  # Retinoic acid-related orphan receptor
        self.neuropeptide_gaba = random.uniform(0.1, 1.0)  # Gamma-Aminobutyric acid

        self.melatonin_secretion = random.uniform(0.1, 1.0)
        self.core_body_temperature = random.uniform(35.5, 37.5)
        self.sleep_wake_cycle = random.uniform(0, 24)
        self.sleep_duration = random.uniform(4, 12)
        self.wake_duration = random.uniform(12, 20)

        self.neuron_astrocyte_interactions = random.uniform(0.1, 1.0)
        self.glutamate_receptors = random.randint(10, 100)
        self.gaba_receptors = random.randint(10, 100)
        self.calcium_signaling = random.uniform(0.01, 0.1)
        self.cAMP_signaling = random.uniform(0.01, 0.1)


        # Ion channels
        self.ion_channels = {
            'leak': {'g': 0.05, 'E': -70.0},
            'Na': {'g': 120.0, 'E': 50.0},
            'K': {'g': 36.0, 'E': -77.0},
            'Ca_T': {'g': 1.0, 'E': 100.0},  # T-type calcium channel
            'Ca_L': {'g': 1.0, 'E': 100.0},  # L-type calcium channel
            'K_Ca': {'g': 1.0, 'E': -90.0},  # Calcium-activated potassium channel
            'K_A': {'g': 1.0, 'E': -90.0},   # A-type potassium channel
            'K_M': {'g': 1.0, 'E': -90.0},   # M-type potassium channel
            'HCN': {'g': 1.0, 'E': -30.0},   # Hyperpolarization-activated cyclic nucleotide-gated channel
        }

        # Neurotransmitter release probability
        self.neurotransmitter_release_probability = 0.5

        # Receptors and synapses
        self.glutamate_receptors = random.randint(10, 100)
        self.gaba_receptors = random.randint(10, 100)
        self.vip_receptors = random.randint(10, 100)  # Vasoactive intestinal peptide receptors
        self.sp_receptors = random.randint(10, 100)    # Substance P receptors

        self.neurotransmitter_storage = random.uniform(0.1, 0.5)
        self.synaptic_cleft_width = random.uniform(20, 50)
        self.neurotransmitter_reuptake_rate = random.uniform(0.01, 0.1)

        # Structural features
        self.soma_diameter = random.uniform(15, 30)
        self.dendrite_diameter = random.uniform(1, 5)
        self.axon_diameter = random.uniform(1, 5)
        self.dendritic_tree_complexity = random.randint(3, 5)
        self.synaptic_vesicles = random.randint(100, 500)
        self.electrical_synapses = random.randint(1, 10)
        self.gap_junctions = random.randint(1, 10)

        # Circadian rhythm related properties
        self.circadian_period = random.uniform(23, 25)  # Hours
        self.circadian_phase = random.uniform(0, 24)  #
        self.circadian_phase = random.uniform(0, 24)  # Hours
        self.circadian_sensitivity = random.uniform(0.1, 1.0)
        self.circadian_amplitude = random.uniform(0.1, 1.0)
        self.light_input = random.uniform(0.1, 1.0)
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

    def integrate_post_synaptic_potentials(self):
        self.membrane_potential += sum(self.post_synaptic_potentials)
        self.post_synaptic_potentials = []

    def add_post_synaptic_potential(self, amplitude):
        self.post_synaptic_potentials.append(amplitude)
    def secrete_neuropeptides(self):
        neuropeptide_amounts = {
            'vip': self.neuropeptide_vip,
            'avp': self.neuropeptide_avp,
            'grpr': self.neuropeptide_grpr,
            'ror': self.neuropeptide_ror,
            'gaba': self.neuropeptide_gaba
        }
        return neuropeptide_amounts

    def regulate_melatonin_secretion(self, light_input):
        if 0 <= light_input < 0.1:  # Low light input
            self.melatonin_secretion = random.uniform(0.8, 1.0)
        elif 0.1 <= light_input < 0.5:  # Moderate light input
            self.melatonin_secretion = random.uniform(0.4, 0.8)
        else:  # High light input
            self.melatonin_secretion = random.uniform(0.0, 0.4)

    def regulate_body_temperature(self):
        if self.sleep_wake_cycle < 12:  # Awake hours
            self.core_body_temperature = random.uniform(36.5, 37.5)
        else:  # Sleep hours
            self.core_body_temperature = random.uniform(35.5, 36.5)

    def update_sleep_wake_cycle(self):
        self.sleep_wake_cycle = (self.sleep_wake_cycle + 1) % 24

    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        self.integrate_post_synaptic_potentials()
        self.fire_if_required()

        for target_neuron in self.local_excitatory_connections:
            target_neuron.receive_excitation(self.id)

        # Update circadian phase and light input
        self.circadian_phase += 1 / 60  # Increment by 1 minute
        if self.circadian_phase >= 24:
            self.circadian_phase = 0

        self.light_input = random.uniform(0.1, 1.0)
        self.regulate_melatonin_secretion(self.light_input)
        self.regulate_body_temperature()
        self.update_sleep_wake_cycle()
        AutoTuneToolkit.optimize_neuron(self)