import numpy as np
from AutoTuneToolkit import AutoTuneToolkit
import time

class PurkinjeCell:
    def __init__(self, activation_function=lambda x: x, learning_rate=0.01, refractory_period=2, firing_threshold=-55, resting_potential=-70, membrane_decay=0.9, dendritic_branches=100):
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
        self.dendritic_tree = [{} for _ in range(dendritic_branches)]

    def connect(self, target_neuron, initial_weight=None, branch=None):
        if initial_weight is None:
            initial_weight = np.random.rand()
        if branch is None:
            branch = np.random.randint(len(self.dendritic_tree))
        self.dendritic_tree[branch][target_neuron] = initial_weight

    def receive_signals(self, inputs):
        if time.time() - self.last_fired < self.refractory_period:
            return

        for branch in self.dendritic_tree:
            branch_potential = sum(branch[neuron] * signal for neuron, signal in inputs)
            self.membrane_potential += branch_potential

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
        for branch in self.dendritic_tree:
            for neuron, signal in inputs:
                if neuron in branch:
                    weight = branch[neuron]
                    new_weight = self.autotune.optimize_weight(weight, signal, self.membrane_potential, self.learning_rate)
                    branch[neuron] = new_weight

    def _send_signals(self):
        for branch in self.dendritic_tree:
            for target_neuron, weight in branch.items():
                target_neuron.receive_signals([(self, self.membrane_potential * weight)])

