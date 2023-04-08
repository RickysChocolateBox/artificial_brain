class Dopamine_GRU:
    def __init__(self):
        self.threshold = 0.5
    
    def release(self, state):
        if state:
            dopamine = state * 0.1
            return dopamine
        else:
            return 0

