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

class TRPM3(IonChannel):
    def __init__(self, conductance, osmotic_pressure, pregnenolone_sulfate):
        super().__init__(conductance)
        self.osmotic_pressure = osmotic_pressure
        self.pregnenolone_sulfate = pregnenolone_sulfate

    def steady_state_values(self, voltage):
        activation = 1 / (1 + np.exp(-(voltage + self.osmotic_pressure + self.pregnenolone_sulfate) / 10))
        return activation, 1

    def time_constants(self, voltage):
        return 1, 1