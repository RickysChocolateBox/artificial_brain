import numpy as np

class IndirectInhibition:
    def __init__(self, num_neurons, num_interneurons, initial_connectivity=None, inhibitory_strength=0.5, interneuron_strength=0.5, min_strength=-1, max_strength=0):
        self.num_neurons = num_neurons
        self.num_interneurons = num_interneurons
        self.inhibitory_strength = inhibitory_strength
        self.interneuron_strength = interneuron_strength

        if initial_connectivity is None:
            self.connectivity_neuron_interneuron = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_interneurons))
            self.connectivity_interneuron_neuron = np.random.uniform(min_strength, max_strength, (self.num_interneurons, self.num_neurons))
        else:
            self.connectivity_neuron_interneuron, self.connectivity_interneuron_neuron = initial_connectivity

    def compute_interneuron_activity(self, neuron_activity):
        interneuron_activity = np.dot(neuron_activity, self.connectivity_neuron_interneuron)
        return interneuron_activity

    def compute_inhibition(self, interneuron_activity):
        inhibition = np.dot(interneuron_activity, self.connectivity_interneuron_neuron)
        return inhibition

    def apply_indirect_inhibition(self, activity_levels):
        # Calculate the interneuron activity based on the neuron activity levels
        interneuron_activity = self.compute_interneuron_activity(activity_levels)

        # Calculate the inhibition based on the interneuron activity levels
        inhibition = self.compute_inhibition(interneuron_activity)

        # Apply the inhibitory effect on the activity levels
        activity_levels -= inhibition * self.inhibitory_strength

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

