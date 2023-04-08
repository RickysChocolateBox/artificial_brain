import numpy as np
class SerotoninSOM:
    def __init__(self, balance_factor):
        self.balance_factor = balance_factor

    def balance_excitation_inhibition(self, activations):
        excitation = np.mean(activations)
        inhibition = np.std(activations)
        balance = (excitation - inhibition) / (excitation + inhibition + self.balance_factor)

        return balance