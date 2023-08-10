import numpy as np

class SpontaneousSynapticActivity:
    def __init__(self, spontaneous_rate, noise_std_dev):
        self.spontaneous_rate = spontaneous_rate
        self.noise_std_dev = noise_std_dev

    # Generate spontaneous synaptic activity
    def generate_activity(self):
        return np.random.normal(self.spontaneous_rate, self.noise_std_dev)

# This class represents the mechanism of spontaneous synaptic activity. The primary function, generate_activity, generates random spontaneous activity based on the spontaneous_rate and noise_std_dev parameters.