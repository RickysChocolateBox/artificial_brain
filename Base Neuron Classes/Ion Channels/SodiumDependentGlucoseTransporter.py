import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class SodiumDependentGlucoseTransporter(IonChannel):
    def __init__(self, conductance, glucose_concentration):
        super().__init__(conductance)
        self.activation = 0.0
        self.glucose_concentration = glucose_concentration

    def steady_state_values(self, glucose_concentration):
        m_inf = 1 / (1 + (5 / glucose_concentration))
        return m_inf

    def update(self, dt):
        m_inf = self.steady_state_values(self.glucose_concentration)
        self.activation += (m_inf - self.activation) * dt

    def compute_current(self, voltage):
        return self.conductance * self.activation * (voltage - 0)