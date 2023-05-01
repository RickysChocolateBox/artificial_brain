import numpy as np

class SpikeTimingDependentPlasticity:
    def __init__(self, learning_rate, stdp_rate, time_window, noise_std_dev):
        self.learning_rate = learning_rate
        self.stdp_rate = stdp_rate
        self.time_window = time_window
        self.noise_std_dev = noise_std_dev

    def spike_time_diff(self, pre_spike_time, post_spike_time):
        return post_spike_time - pre_spike_time

    def update_synaptic_strength(self, synaptic_strength, spike_time_difference):
        noise = np.random.normal(0, self.noise_std_dev)
        spike_time_difference += noise

        if abs(spike_time_difference) <= self.time_window:
            synaptic_strength += self.learning_rate * self.stdp_rate * spike_time_difference

        return synaptic_strength

