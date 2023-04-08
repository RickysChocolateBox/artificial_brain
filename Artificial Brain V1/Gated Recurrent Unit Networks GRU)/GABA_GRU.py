class GABA_GRU:
    def __init__(self):
        self.inhibitory_factor = 0.1
    
    def inhibit(self, state):
        if state:
            return state * self.inhibitory_factor
        else:
            return 0

