import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class KATPChannel(IonChannel):
    def __init__(self, conductance):
        super().__init__(conductance)
        self.activation = 0.0
        self.inactivation = 1.0

    def steady_state_values(self, voltage):
        n_inf = 1 / (1 + np.exp(-(voltage + 50) / 10))
        return n_inf

    def time_constants(self, voltage):
        tau_n = 7
        return tau_n

    def update(self, voltage, dt):
        n_inf = self.steady_state_values(voltage)
        tau_n = self.time_constants(voltage)
        self.activation += (n_inf - self.activation) * dt / tau_n

    def compute_current(self, voltage):
        return self.conductance * self.activation**4 * (voltage + 90)

class BKChannel(IonChannel):
    def __init__(self, conductance):
        super().__init__(conductance)
        self.activation = 0.0
        self.inactivation = 1.0

    def steady_state_values(self, voltage):
        m_inf = 1 / (1 + np.exp(-(voltage + 30) / 10))
        h_inf = 1 / (1 + np.exp((voltage + 50) / 10))
        return m_inf, h_inf

    def time_constants(self, voltage):
        tau_m = 3
        tau_h = 15
        return tau_m, tau_h

    def update(self, voltage, dt):
        m_inf, h_inf = self.steady_state_values(voltage)
        tau_m, tau_h = self.time_constants(voltage)
        self.activation += (m_inf - self.activation) * dt / tau_m
        self.inactivation += (h_inf - self.inactivation) * dt / tau_h

    def compute_current(self, voltage):
        return self.conductance * self.activation**3 * self.inactivation * (voltage - 60)