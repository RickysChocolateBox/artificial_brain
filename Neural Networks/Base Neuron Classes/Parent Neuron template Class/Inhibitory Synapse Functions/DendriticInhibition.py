import numpy as np

class DendriticInhibition:
    def __init__(self, num_neurons, dendritic_inhibition_strength=0.5, dendritic_tree=None):
        self.num_neurons = num_neurons
        self.dendritic_inhibition_strength = dendritic_inhibition_strength
        self.dendritic_tree = dendritic_tree if dendritic_tree else self.generate_dendritic_tree()

    def generate_dendritic_tree(self):
        dendritic_tree = {}
        for neuron in range(self.num_neurons):
            dendritic_tree[neuron] = [np.random.randint(self.num_neurons) for _ in range(np.random.randint(1, 4))]
        return dendritic_tree

    def apply_dendritic_inhibition(self, activity_levels):
        # Calculate dendritic inhibition effect for each neuron
        dendritic_inhibition_effect = np.zeros(self.num_neurons)

        for neuron, connected_neurons in self.dendritic_tree.items():
            inhibitory_activity = 0
            for connected_neuron in connected_neurons:
                inhibitory_activity += activity_levels[connected_neuron] * self.dendritic_inhibition_strength
            dendritic_inhibition_effect[neuron] = inhibitory_activity

        # Apply dendritic inhibition to each neuron's activity level
        activity_levels -= dendritic_inhibition_effect

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

