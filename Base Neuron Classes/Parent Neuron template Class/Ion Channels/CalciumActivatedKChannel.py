import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class CalciumActivatedKChannel(IonChannel):
    def __init__(self, conductance, calcium_concentration):
        self.conductance = conductance
        self.activation = 0.0
        self.calcium_concentration = calcium_concentration

    def steady_state_values(self):
        a_inf = self.calcium_concentration / (self.calcium_concentration + 0.5)
        return a_inf

    def time_constants(self):
        tau_a = 1 / (self.calcium_concentration + 0.5)
        return tau_a

    def update(self, dt):
        a_inf = self.steady_state_values()
        tau_a = self.time_constants()
        self.activation += (a_inf - self.activation) * dt / tau_a
    def compute_current(self, voltage):
        return self.conductance * self.activation * (voltage + 90)