import numpy as np
from AutoTuneToolkit import AutoTuneToolkit

class DendriticCompartment:
        def __init__(self, voltage=-70, threshold=-45, spike_duration=2, calcium_threshold=50, nmda_threshold=75):
            self.voltage = voltage
            self.threshold = threshold
            self.spike_duration = spike_duration
            self.calcium_threshold = calcium_threshold
            self.nmda_threshold = nmda_threshold
            self.spike_time = None
            self.calcium_spike_time = None
            self.nmda_spike_time = None

        def update(self, voltage, delta_t):
            self.voltage += delta_t * (voltage - self.voltage)

        def spike_occurred(self):
            return self.spike_time is not None

        def reset_spike(self):
            self.spike_time = None

        def calcium_spike_occurred(self):
            return self.calcium_spike_time is not None

        def reset_calcium_spike(self):
            self.calcium_spike_time = None

        def nmda_spike_occurred(self):
            return self.nmda_spike_time is not None

        def reset_nmda_spike(self):
         self.nmda_spike_time = None

class BaseNeuron:
    def __init__(self, input_synapses, output_synapses, dendritic_compartments, resting_potential=-70, threshold=-55, 
                 refractory_period=2, capacitance=1, time_constant=20, synapse_strength=1.0, stdp_time_window=20, 
                 stdp_potentiation=0.01, stdp_depression=0.002, axon_length=1000, soma_radius=10, 
                 calcium_concentration=0.0, calcium_decay_rate=0.01, calcium_spike_threshold=0.2, 
                 nmda_enabled=False, nmda_alpha=0.5, nmda_beta=0.5, nmda_gamma=0.1, nmda_v0=-70.0, 
                 nmda_mg_concentration=1.0, nmda_mg_saturation=0.5, calcium_activated_k_channels=None,
                 calcium_activated_k_channel_gmax=0.0, calcium_activated_k_channel_ec50=1.0, 
                 calcium_activated_k_channel_hill=1.0, calcium_activated_k_channel_forward_rate=1.0, 
                 calcium_activated_k_channel_backward_rate=1.0):
        
        # Common properties
        self.voltage = -70.0
        self.threshold = -55.0
        self.resting_potential = -70.0
        self.refractory_period = 2.0
        self.time_since_last_spike = float('inf')
        self.current_time = 0.0
        self.synaptic_inputs = []
        self.synaptic_outputs = []
        self.synaptic_weights = {}
        self.AutoTuneToolkit = AutoTuneToolkit
        
        # Customizable properties
        self.custom_properties = {}
        
        # Dendritic properties
        self.dendritic_compartments = []
        self.dendritic_spikes = []
        self.calcium_spikes = []
        self.nmda_spikes = []
        self.input_synapses = input_synapses
        self.output_synapses = output_synapses
        self.dendritic_compartments = dendritic_compartments
        self.voltage = resting_potential
        self.resting_potential = resting_potential
        self.threshold = threshold
        self.refractory_period = refractory_period
        self.capacitance = capacitance
        self.time_constant = time_constant
        self.synapse_strength = synapse_strength
        self.stdp_time_window = stdp_time_window
        self.stdp_potentiation = stdp_potentiation
        self.stdp_depression = stdp_depression
        self.axon_length = axon_length
        self.soma_radius = soma_radius
        self.current_time = 0
        self.time_since_last_spike = -np.inf
        self.dendritic_spikes = []
        self.calcium_spikes = []
        self.nmda_spikes = []
        
        # Ion channel properties
        self.sodium_channels = []
        self.potassium_channels = []
        self.leak_channels = []
        self.calcium_activated_k_channels = calcium_activated_k_channels
        self.calcium_activated_k_channel_gmax = calcium_activated_k_channel_gmax
        self.calcium_activated_k_channel_ec50 = calcium_activated_k_channel_ec50
        self.calcium_activated_k_channel_hill = calcium_activated_k_channel_hill
        self.calcium_activated_k_channel_forward_rate = calcium_activated_k_channel_forward_rate
        self.calcium_activated_k_channel_backward_rate = calcium_activated_k_channel_backward_rate

       # Calcium properties
        self.calcium_concentration = calcium_concentration
        self.calcium_decay_rate = calcium_decay_rate
        self.calcium_spike_threshold = calcium_spike_threshold
        
        # NMDA receptor properties
        self.nmda_enabled = nmda_enabled
        self.nmda_alpha = nmda_alpha
        self.nmda_beta = nmda_beta
        self.nmda_gamma = nmda_gamma
        self.nmda_v0 = nmda_v0
        self.nmda_mg_concentration = nmda_mg_concentration
        self.nmda_mg_saturation = nmda_mg_saturation

        # Calcium-activated potassium channels
        if calcium_activated_k_channels is None:
            self.calcium_activated_k_channels = []
        else:
            self.calcium_activated_k_channels = calcium_activated_k_channels

        # Synaptic plasticity
        self.stdp_enabled = False
        self.stdp_time_window = 20.0
        self.stdp_potentiation = 0.01
        self.stdp_depression = 0.01
        self.dendritic_compartments = [DendriticCompartment() for _ in range(dendritic_compartments)]
                # Spike-frequency adaptation
        self.sfa_enabled = False
        self.sfa_time_constant = 100.0
        self.sfa_gain = 0.01
        self.sfa_current = 0.0
        
        # Backpropagation of action potentials
        self.bpa_enabled = False
        self.bpa_compartments = []
        self.bpa_delay = 0.1
        
        # Axonal conduction delays
        self.axonal_delays = []
        self.axonal_speed = 100.0

    def set_property(self, property_name, value):
        self.custom_properties[property_name] = value
        
    def get_property(self, property_name):
        return self.custom_properties.get(property_name, None)

    def add_dendritic_compartment(self, compartment):
        self.dendritic_compartments.append(compartment)

    def add_ion_channel(self, channel_type, channel):
        if channel_type == 'sodium':
            self.sodium_channels.append(channel)
        elif channel_type == 'potassium':
            self.potassium_channels.append(channel)
        elif channel_type == 'leak':
            self.leak_channels.append(channel)
        else:
            raise ValueError("Invalid channel type")

    def update(self, delta_t):
        self.current_time += delta_t
        self.update_voltage(delta_t)
        
        if self.voltage >= self.threshold and self.time_since_last_spike >= self.refractory_period:
            self.generate_action_potential()
            self.time_since_last_spike = 0
        else:
            self.time_since_last_spike += delta_t

        self.update_dendritic_spikes(delta_t)

    def update_voltage(self, delta_t):
        # Update voltage based on ion channel dynamics
        ion_currents = []
        for channel in self.sodium_channels:
            ion_currents.append(channel.get_current(self.voltage))
        for channel in self.potassium_channels:
            ion_currents.append(channel.get_current(self.voltage))
        for channel in self.leak_channels:
            ion_currents.append(channel.get_current(self.voltage))
        total_current = sum(ion_currents)
        self.voltage += total_current * delta_t

    def generate_action_potential(self):
        # Reset voltage and propagate the action potential
        self.voltage = self.resting_potential
        self.propagate_action_potential(self.synaptic_outputs)

    def propagate_action_potential(self, connected_neurons):
        for neuron in connected_neurons:
            neuron.receive_spike(self.synaptic_weights[neuron])

    def receive_spike(self, synaptic_weight):
        self.voltage += synaptic_weight

        # Update synaptic weights if STDP is enabled
        if self.stdp_enabled:
            self.update_synaptic_weights(synaptic_weight)

    def update_synaptic_weights(self, synaptic_weight):
        time_since_last_spike = self.current_time - self.time_since_last_spike

        if time_since_last_spike < self.stdp_time_window:
            # Potentiation (strengthening the synapse)
            synaptic_weight += self.stdp_potentiation
        else:
            # Depression (weakening the synapse)
            synaptic_weight -= self.stdp_depression

    def update_dendritic_spikes(self, delta_t):
        # Update dendritic spikes and calcium spikes based on the article's concepts
        for compartment in self.dendritic_compartments:
            compartment.update(self.voltage, delta_t)

            if compartment.spike_occurred():
                self.dendritic_spikes.append((self.current_time, compartment))
                if compartment.calcium_spike_occurred():
                    self.calcium_spikes.append((self.current_time, compartment))
                if compartment.nmda_spike_occurred():
                    self.nmda_spikes.append((self.current_time, compartment))
    def step(self, delta_t, input_current):
        # Update dendritic compartments
        self.update_dendritic_spikes(delta_t)

        # Update voltage
        self.voltage = self.leakage_current() + self.capacitive_current(input_current) + self.synaptic_current()

        # Check if the neuron should spike
        if self.voltage > self.threshold and (self.current_time - self.time_since_last_spike) > self.refractory_period:
            self.fire_spike()

        # Update time
        self.current_time += delta_t

    def leakage_current(self):
        return self.resting_potential - (self.voltage / self.time_constant)

    def capacitive_current(self, input_current):
        return (input_current / self.capacitance) * self.time_constant

    def synaptic_current(self):
        total_current = 0
        for synapse in self.input_synapses:
            total_current += synapse.transmit(self.synapse_strength)
        return total_current

    def fire_spike(self):
        self.voltage = self.resting_potential
        self.time_since_last_spike = self.current_time
        for synapse in self.output_synapses:
            synapse.spike_occurred(self.current_time)
            self.update_synaptic_weights(synapse.weight)

    def update_synaptic_weights(self, synaptic_weight):
        time_since_last_spike = self.current_time - self.time_since_last_spike

        if time_since_last_spike < self.stdp_time_window:
            # Potentiation (strengthening the synapse)
            synaptic_weight += self.stdp_potentiation
        else:
            # Depression (weakening the synapse)
            synaptic_weight -= self.stdp_depression

    def update_dendritic_spikes(self, delta_t):
        # Update dendritic spikes and calcium spikes based on the article's concepts
        for compartment in self.dendritic_compartments:
            compartment.update(self.voltage, delta_t)

            if compartment.spike_occurred():
                self.dendritic_spikes.append(compartment.spike_time)
                compartment.reset_spike()

            if compartment.calcium_spike_occurred():
                self.calcium_spikes.append(compartment.calcium_spike_time)
                compartment.reset_calcium_spike()

            if compartment.nmda_spike_occurred():
                self.nmda_spikes.append(compartment.nmda_spike_time)
                compartment.reset_nmda_spike()
def simulate_neuron(neuron, input_data, delta_t=0.1):
    output_data = []
    for input_current in input_data:
        neuron.step(delta_t, input_current)
        output_data.append(neuron.voltage)
    return np.array(output_data)

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def evaluate_neuron(neuron_class, neuron_params, input_data, target_data):
    neuron = neuron_class(**neuron_params)
    output_data = simulate_neuron(neuron, input_data)
    return -mean_squared_error(target_data, output_data)

def optimize_neuron(neuron_class, param_space, input_data, target_data):
    # Instantiate an AutoTune object
    AutoTuneToolkit = AutoTuneToolkit(lambda params: evaluate_neuron(neuron_class, params, input_data, target_data))

    # Set the parameter search space
    AutoTuneToolkit.set_param_space(param_space)

    # Run the optimization process
    best_params, best_score = AutoTuneToolkit.optimize()

    # Print the best parameters and their corresponding score
    print("Best parameters found: ", best_params)
    print("Best score: ", best_score)

    # Create a neuron with the optimized parameters
    optimized_neuron = neuron_class(**best_params)
    return optimized_neuron

# Load input data and target data
input_data = ...  # Your input data goes here
target_data = ...  # Your target data goes here

# Define the parameter search space for AutoTune
param_space = {
    # ... (Your existing parameter space definition)
}

# Optimize the BaseNeuron
optimized_neuron = optimize_neuron(BaseNeuron, param_space, input_data, target_data)