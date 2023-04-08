class Serotonin_GRU:
    def __init__(self):
        self.balance_factor = 0.5
    
    def balance(self, excitation, inhibition):
        balance = (excitation - inhibition) * self.balance_factor
        return balance
