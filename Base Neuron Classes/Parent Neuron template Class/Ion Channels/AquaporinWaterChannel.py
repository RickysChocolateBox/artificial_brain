import numpy as np

class IonChannel:
    def __init__(self, conductance):
        self.conductance = conductance

    def compute_current(self, voltage):
        pass
class AquaporinWaterChannel(IonChannel):
    def __init__(self, conductance, osmotic_gradient):
        super().__init__(conductance)
        self.osmotic_gradient = osmotic_gradient

    def compute_current(self, voltage):
        # Aquaporin channels are not directly voltage-dependent, but the flow depends on the osmotic gradient
        return self.conductance * self.osmotic_gradient