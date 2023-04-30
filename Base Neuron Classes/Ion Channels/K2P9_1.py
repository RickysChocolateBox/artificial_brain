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
class K2P9_1(IonChannel):
    def __init__(self, conductance, pH):
        super().__init__(conductance)
        self.pH = pH

    def steady_state_values(self, voltage):
        activation = 1 / (1 + np.exp((voltage - self.pH) / 10))
        return activation, 1

    def time_constants(self, voltage):
        return 1, 1
