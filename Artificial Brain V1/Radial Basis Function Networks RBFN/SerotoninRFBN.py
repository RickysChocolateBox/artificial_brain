import numpy as np
class SerotoninRFBN:
    def __init__(self, balance_factor):
        self.balance_factor = balance_factor
    
    def balance_excitation_inhibition(self, neurons):
        excitatory = np.where(neurons > 0, neurons, 0)
        inhibitory = np.where(neurons < 0, neurons, 0)
        balance = self.balance_factor * (np.sum(excitatory) / (np.sum(excitatory) - np.sum(inhibitory)))
        neurons = balance * (excitatory - inhibitory)
        return neurons
