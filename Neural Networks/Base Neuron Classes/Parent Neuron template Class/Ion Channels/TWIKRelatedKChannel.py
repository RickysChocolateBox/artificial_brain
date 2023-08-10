import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class TWIKRelatedKChannel(IonChannel):
    def __init__(self, conductance):
        self.conductance = conductance
        self.activation = 0.0

    def steady_state_values(self, voltage):
        a_inf = 1 / (1 + np.exp(-(voltage + 40) / 20))
        return a_inf

    def time_constants(self, voltage):
        tau_a = 1 / (np.exp((voltage + 40) / 20) + np.exp(-(voltage + 40) / 20))
        return tau_a

    def update(self, voltage, dt):
        a_inf = self.steady_state_values(voltage)
        tau_a = self.time_constants(voltage)
        self.activation += (a_inf - self.activation) * dt / tau_a

    def compute_current(self, voltage):
        return self.conductance * self.activation * (voltage + 90)
