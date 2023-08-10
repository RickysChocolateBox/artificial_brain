import numpy as np

class PhasicInhibition:
    def __init__(self, num_neurons, initial_connectivity=None, inhibitory_strength=0.5, phasic_strength=0.3, min_strength=-1, max_strength=0, phase_duration=5):
        self.num_neurons = num_neurons
        self.inhibitory_strength = inhibitory_strength
        self.phasic_strength = phasic_strength
        self.phase_duration = phase_duration

        if initial_connectivity is None:
            self.phasic_connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.phasic_connectivity = initial_connectivity
        self.phase_counter = 0

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.phasic_connectivity
        return inhibition

    def apply_phasic_inhibition(self, activity_levels):
        # Calculate the total inhibition for each neuron pair
        total_inhibition = np.zeros((self.num_neurons, self.num_neurons))
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    pre_synaptic_activity = activity_levels[i]
                    post_synaptic_activity = activity_levels[j]
                    total_inhibition[i, j] = self.compute_inhibition(pre_synaptic_activity, post_synaptic_activity)

        # Apply the overall phasic inhibition effect
        phasic_inhibition_effect = np.dot(total_inhibition, activity_levels) * self.phasic_strength

        # Update the phase counter
        self.phase_counter += 1
        if self.phase_counter >= self.phase_duration:
            self.phase_counter = 0
            phasic_inhibition_effect *= -1  # Reverse the inhibition effect at the end of each phase

        # Modify the activity levels based on the phasic inhibition
        activity_levels -= phasic_inhibition_effect

        # Ensure the activity levels remain in the valid range [0, 1]
        activity_levels = np.clip(activity_levels, 0, 1)

        return activity_levels

