import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class NaK2ClCotransporter(IonChannel):
    def __init__(self, conductance, na_concentration, k_concentration, cl_concentration):
        super().__init__(conductance)
        self.na_concentration = na_concentration
        self.k_concentration = k_concentration
        self.cl_concentration = cl_concentration

    def compute_current(self, voltage):
        # Assuming constant conductance and ion reversal potential
        return self.conductance * ((self.na_concentration + self.k_concentration) * 2 * self.cl_concentration) * (voltage - 0)