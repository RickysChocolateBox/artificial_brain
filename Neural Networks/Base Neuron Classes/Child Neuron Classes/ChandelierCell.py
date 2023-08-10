import numpy as np
from AutoTuneToolkit import AutoTuneToolkit
import time

class ChandelierCell:
    def __init__(self, activation_function=lambda x: x, learning_rate=0.01, refractory_period=1, firing_threshold=-50, resting_potential=-70, membrane_decay=0.95, axon_terminal_count=100):
        self.activation_function = activation_function
        self.learning_rate = learning_rate
        self.membrane_potential = resting_potential
        self.connections = {}
        self.AutoTuneToolkit = AutoTuneToolkit()
        self.last_fired = -np.inf
        self.refractory_period = refractory_period
        self.firing_threshold = firing_threshold
        self.resting_potential = resting_potential
        self.membrane_decay = membrane_decay
        self.axon_terminals = [{} for _ in range(axon_terminal_count)]

    def connect(self, target_neuron, initial_weight=None, terminal=None):
        if initial_weight is None:
            initial_weight = np.random.rand()
        if terminal is None:
            terminal = np.random.randint(len(self.axon_terminals))
        self.axon_terminals[terminal][target_neuron] = initial_weight

    def receive_signals(self, inputs):
        if time.time() - self.last_fired < self.refractory_period:
            return

        for input_neuron, signal in inputs:
            self.membrane_potential += self.connections.get(input_neuron, 0) * signal

        self.membrane_potential = self.activation_function(self.membrane_potential)
        self._update_weights(inputs)

        if self.membrane_potential >= self.firing_threshold:
            self._send_signals()
            self.membrane_potential = self.resting_potential
            self.last_fired = time.time()
        else:
            self.membrane_potential *= self.membrane_decay
            self.membrane_potential = max(self.membrane_potential, self.resting_potential)

    def _update_weights(self, inputs):
        for neuron, signal in inputs:
            if neuron in self.connections:
                weight = self.connections[neuron]
                new_weight = self.autotune.optimize_weight(weight, signal, self.membrane_potential, self.learning_rate)
                self.connections[neuron] = new_weight

    def _send_signals(self):
        for terminal in self.axon_terminals:
            for target_neuron, weight in terminal.items():
                target_neuron.receive_signals([(self, self.membrane_potential * weight)])
