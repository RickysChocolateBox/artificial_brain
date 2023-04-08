class Norepinephrine_GRU:
    def __init__(self):
        self.max_speed = 10
    
    def adjust_speed(self, sequence, gate_complexity):
        speed = self.max_speed / (gate_complexity + 1)
        if len(sequence) > 10:
            speed *= 1.5
        return speed

