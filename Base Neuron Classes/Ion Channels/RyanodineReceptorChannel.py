import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class RyanodineReceptorChannel(IonChannel):
    def __init__(self, conductance):
        super().__init__(conductance)
        self.activation = 0.0

    def steady_state_values(self, voltage, ca_concentration):
        m_inf = 1 / (1 + (ca_concentration / 0.3)**-3)
        return m_inf

    def update(self, voltage, dt, ca_concentration):
        m_inf = self.steady_state_values(voltage, ca_concentration)
        self.activation += (m_inf - self.activation) * dt

    def compute_current(self, voltage):
        return self.conductance * self.activation * (voltage - 120)
