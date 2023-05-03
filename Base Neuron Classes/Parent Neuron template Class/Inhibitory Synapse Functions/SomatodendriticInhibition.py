import numpy as np

class SomatodendriticInhibition:
    def __init__(self, num_neurons, somatodendritic_inhibition_strength=0.5, soma_strength=0.3, dendritic_strength=0.7):
        self.num_neurons = num_neurons
        self.somatodendritic_inhibition_strength = somatodendritic_inhibition_strength
        self.soma_strength = soma_strength
        self.dendritic_strength = dendritic_strength
        self.inhibitory_connectivity_soma = np.random.uniform(-1, 0, (self.num_neurons, self.num_neurons))
        self.inhibitory_connectivity_dendritic = np.random.uniform(-1, 0, (self.num_neurons, self.num_neurons))

    def apply_somatodendritic_inhibition(self, activity_levels):
        # Calculate soma inhibition effect for each neuron
        soma_inhibition_effect = np.dot(self.inhibitory_connectivity_soma, activity_levels) * self.soma_strength

        # Calculate dendritic inhibition effect for each neuron
        dendritic_inhibition_effect = np.dot(self.inhibitory_connectivity_dendritic, activity_levels) * self.dendritic_strength

        # Combine soma and dendritic inhibition effects
        somatodendritic_inhibition_effect = soma_inhibition_effect + dendritic_inhibition_effect

        # Apply somatodendritic inhibition strength
        somatodendritic_inhibition_effect *= self.somatodendritic_inhibition_strength

        # Modify the activity levels based on the somatodendritic inhibition
        activity_levels -= somatodendritic_inhibition_effect

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

