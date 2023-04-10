import numpy as np
class SerotoninFNN:
    def __init__(self, balance_factor):
        self.balance_factor = balance_factor

    def balance_neurons(self, input_data):
        excitation = np.sum(input_data > 0)
        inhibition = np.sum(input_data < 0)
        balance = (excitation - inhibition) * self.balance_factor
        return balance
