class SerotoninHopfieldNetworks:
    def __init__(self, balance_factor):
        self.balance_factor = balance_factor
        
    def balance_network(self, network):
        excitatory_sum = 0
        inhibitory_sum = 0
        
        for neuron in network:
            if neuron.excited:
                excitatory_sum += neuron.activation
            else:
                inhibitory_sum += neuron.activation
                
        balance = (excitatory_sum - inhibitory_sum) / len(network)
        if balance < 0:
            for neuron in network:
                neuron.inhibit()
        else:
            for neuron in network:
                neuron.excite()

