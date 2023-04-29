import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class TRPChannel(IonChannel):
    def __init__(self, conductance):
        super().__init__(conductance)
        self.activation = 0.0
        self.inactivation = 1.0

    def steady_state_values(self, voltage):
        m_inf = 1 / (1 + np.exp(-(voltage + 40) / 10))
        h_inf = 1 / (1 + np.exp((voltage + 60) / 12))
        return m_inf, h_inf

    def time_constants(self, voltage):
        tau_m = 1 / (3 * (np.exp(-(voltage + 50) / 20) + np.exp((voltage + 50) / 20)))
        tau_h = 1 / (3 * (np.exp(-(voltage + 50) / 20) + np.exp((voltage + 50) / 20)))
        return tau_m, tau_h

    def update(self, voltage, dt):
        m_inf, h_inf = self.steady_state_values(voltage)
        tau_m, tau_h = self.time_constants(voltage)
        self.activation += (m_inf - self.activation) * dt / tau_m
        self.inactivation += (h_inf - self.inactivation) * dt / tau_h

    def compute_current(self, voltage):
        return self.conductance * self.activation * self.inactivation * (voltage - 30)