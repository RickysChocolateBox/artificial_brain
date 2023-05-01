import numpy as np

class NeuronGliaInteractions:
    def __init__(self, neuron_count, glia_count, interaction_strength, learning_rate, activation_function):
        self.neuron_count = neuron_count
        self.glia_count = glia_count
        self.interaction_strength = interaction_strength
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.neuron_glia_matrix = np.random.rand(neuron_count, glia_count) * interaction_strength

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_neuron_glia_matrix(self, neuron_activation, glia_activation):
        delta_matrix = np.outer(neuron_activation, glia_activation) * self.learning_rate
        self.neuron_glia_matrix += delta_matrix

    def update_glia(self, neuron_activation):
        glia_activation = np.dot(neuron_activation, self.neuron_glia_matrix)
        glia_activation = self.apply_activation_function(glia_activation)
        return glia_activation

    def update_neuron(self, glia_activation):
        neuron_activation = np.dot(glia_activation, self.neuron_glia_matrix.T)
        neuron_activation = self.apply_activation_function(neuron_activation)
        return neuron_activation

    def neuron_glia_interaction(self, neuron_activation):
        glia_activation = self.update_glia(neuron_activation)
        updated_neuron_activation = self.update_neuron(glia_activation)
        self.update_neuron_glia_matrix(neuron_activation, glia_activation)
        return updated_neuron_activation

