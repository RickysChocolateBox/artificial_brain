import random
from collections import defaultdict
from AutoTuneToolkit import AutoTuneToolkit

class VentralCochlearNucleusNeuron:
    def __init__(self, id):
        self.id = id
        self.membrane_potential = -70.0
        self.resting_potential = -70.0
        self.threshold_potential = -55.0
        self.refractory_period = 2.0
        self.refractory_timer = 0.0
        self.local_inhibitory_connections = []
        self.local_excitatory_connections = []
        self.autotune_toolkit = AutoTuneToolkit()

        self.ion_channels = {
            'leak': {'g': 0.05, 'E': -70.0},
            'Na': {'g': 120.0, 'E': 50.0},
            'K': {'g': 36.0, 'E': -77.0},
        }

        self.frequency_tuning = defaultdict(float)
        self.auditory_input = defaultdict(float)
        self.auditory_output = defaultdict(float)
        self.synaptic_plasticity = defaultdict(float)
        self.action_potential_history = []

    def connect_inhibitory(self, target_neuron):
        self.local_inhibitory_connections.append(target_neuron)

    def connect_excitatory(self, target_neuron):
        self.local_excitatory_connections.append(target_neuron)

    def receive_auditory_input(self, frequency, input_strength):
        self.auditory_input[frequency] += input_strength

    def process_auditory_input(self):
        for frequency, input_strength in self.auditory_input.items():
            self.frequency_tuning[frequency] += input_strength
            self.membrane_potential += input_strength * self.frequency_tuning[frequency]

    def send_auditory_output(self):
        for target_neuron in self.local_excitatory_connections:
            target_neuron.receive_auditory_output(self.auditory_output)

    def receive_auditory_output(self, auditory_output):
        for frequency, output_strength in auditory_output.items():
            self.auditory_input[frequency] += output_strength

    def fire_if_required(self):
        if self.membrane_potential >= self.threshold_potential:
            self.send_auditory_output()
            self.membrane_potential = self.resting_potential
            self.enter_refractory_period()
            self.action_potential_history.append(1)
        else:
            self.autotune_toolkit.auto_tune_ion_channels(self.ion_channels)
            self.action_potential_history.append(0)

    def enter_refractory_period(self):
        self.membrane_potential = self.resting_potential
        self.refractory_timer = self.refractory_period

    def update_synaptic_weights(self):
        for frequency, weight in self.synaptic_plasticity.items():
            self.synaptic_plasticity[frequency] += random.uniform(-0.1, 0.1)

    def simulate_time_step(self):
        if self.refractory_timer > 0:
            self.refractory_timer -= 1
            return

        self.process_auditory_input()
        self.fire_if_required()
        self.update_synaptic_weights()
        self.autotune_toolkit.auto_tune_ion_channels(self.ion_channels)

        # Truncate action_potential_history to keep only the most recent events
        if len(self.action_potential_history) > 1000:
            self.action_potential_history.pop(0)
