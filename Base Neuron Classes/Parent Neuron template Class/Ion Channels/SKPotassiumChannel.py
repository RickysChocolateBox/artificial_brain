import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance
        self.activation = 0
        self.inactivation = 0

    def steady_state_values(self, voltage):
        pass

    def time_constants(self, voltage):
        pass

    def update(self, voltage, dt):
        self.activation, self.inactivation = self.steady_state_values(voltage)
        tau_activation, tau_inactivation = self.time_constants(voltage)
        self.activation += dt / tau_activation
        self.inactivation += dt / tau_inactivation

    def compute_current(self, voltage):
        return self.conductance * self.activation * self.inactivation * (voltage - self.reversal_potential)
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
