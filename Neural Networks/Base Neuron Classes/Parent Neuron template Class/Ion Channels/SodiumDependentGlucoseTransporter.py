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