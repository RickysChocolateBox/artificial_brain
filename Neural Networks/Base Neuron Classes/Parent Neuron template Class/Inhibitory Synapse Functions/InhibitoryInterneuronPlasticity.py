import numpy as np

class InhibitoryInterneuronPlasticity:
    def __init__(self, num_neurons, initial_connectivity=None, min_strength=-1, max_strength=0, learning_rate=0.1, tau_pos=20, tau_neg=20, a_pos=1, a_neg=1):
        self.num_neurons = num_neurons
        self.learning_rate = learning_rate
        self.tau_pos = tau_pos
        self.tau_neg = tau_neg
        self.a_pos = a_pos
        self.a_neg = a_neg

        if initial_connectivity is None:
            self.connectivity = np.random.uniform(min_strength, max_strength, (self.num_neurons, self.num_neurons))
        else:
            self.connectivity = initial_connectivity

        self.spike_times = np.zeros(self.num_neurons)

    def compute_inhibition(self, pre_synaptic_activity, post_synaptic_activity):
        inhibition = np.outer(pre_synaptic_activity, post_synaptic_activity)
        inhibition *= self.connectivity
        return inhibition

    def update_spike_times(self, activity_levels, t):
        for i in range(self.num_neurons):
            if activity_levels[i] > 0:
                self.spike_times[i] = t

    def apply_stdp(self, activity_levels, t):
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if i != j:
                    delta_t = self.spike_times[i] - self.spike_times[j]

                    if delta_t > 0:
                        delta_w = self.a_pos * np.exp(-delta_t / self.tau_pos)
                    else:
                        delta_w = -self.a_neg * np.exp(delta_t / self.tau_neg)

                    self.connectivity[i, j] += self.learning_rate * delta_w

        return activity_levels

    def update(self, activity_levels, t):
        self.update_spike_times(activity_levels, t)
        self.apply_stdp(activity_levels, t)
        return activity_levels
