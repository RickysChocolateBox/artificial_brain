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

class KCNA5(IonChannel):
    def __init__(self, conductance):
        super().__init__(conductance)

    def steady_state_values(self, voltage):
        activation = 1 / (1 + np.exp(-(voltage + 20) / 10))
        inactivation = 1 / (1 + np.exp((voltage + 90) / 10))
        return activation, inactivation

    def time_constants(self, voltage):
        tau_activation = 1
        tau_inactivation = 100 + 50 * np.exp(-(voltage + 20) / 20)
        return tau_activation, tau_inactivation
