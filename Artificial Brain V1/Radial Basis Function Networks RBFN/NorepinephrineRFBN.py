import numpy as np
class NorepinephrineRFBN:
    def __init__(self, speed_factor):
        self.speed_factor = speed_factor
    
    def adjust_speed(self, input_data):
        speed = 1 / (1 + np.exp(-self.speed_factor * (np.mean(input_data) - 0.5)))
        return speed
