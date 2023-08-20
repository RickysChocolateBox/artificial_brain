import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class HCNChannel(IonChannel):
    def __init__(self, conductance):
        self.conductance = conductance
        self.activation = 0.0

    def steady_state_values(self, voltage):
        m_inf = 1 / (1 + np.exp((voltage + 50) / 10))
        return m_inf

    def time_constants(self, voltage):
        tau_m = 1 / (np.exp((voltage + 40) / 10) + np.exp(-(voltage + 40) / 10))
        return tau_m

    def update(self, voltage, dt):
        m_inf = self.steady_state_values(voltage)
        tau_m = self.time_constants(voltage)
        self.activation += (m_inf - self.activation) * dt / tau_m

    def compute_current(self, voltage):
        return self.conductance * self.activation * (voltage + 35)