import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class SKPotassiumChannel(IonChannel):
    def __init__(self, conductance, calcium_concentration):
        super().__init__(conductance)
        self.activation = 0.0
        self.calcium_concentration = calcium_concentration

    def steady_state_values(self, calcium_concentration):
        m_inf = 1 / (1 + (0.3 / calcium_concentration)**4)
        return m_inf

    def update(self, dt):
        m_inf = self.steady_state_values(self.calcium_concentration)
        self.activation += (m_inf - self.activation) * dt

    def compute_current(self, voltage):
        return self.conductance * self.activation * (voltage - (-80))
