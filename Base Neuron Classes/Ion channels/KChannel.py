import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class KChannel(IonChannel):
    def __init__(self, conductance):
        super().__init__(conductance)
        self.activation = 0.0
        self.inactivation = 1.0

    def steady_state_values(self, voltage):
        n_inf = 1 / (1 + np.exp(-(voltage + 55) / 10))
        return n_inf

    def time_constants(self, voltage):
        tau_n = 5
        return tau_n

    def update(self, voltage, dt):
        n_inf = self.steady_state_values(voltage)
        tau_n = self.time_constants(voltage)
        self.activation += (n_inf - self.activation) * dt / tau_n

    def compute_current(self, voltage):
        return self.conductance * self.activation**4 * (voltage + 80)

