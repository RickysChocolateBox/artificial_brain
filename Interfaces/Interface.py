class Interface:
    def __init__(self, adaptive_neural_network, protobrain_models):
        self.adaptive_neural_network = adaptive_neural_network
        self.protobrain_models = protobrain_models
        self.connections = self.initialize_connections()

    def initialize_connections(self):
        connections = {}
        for region, protobrain_model in self.protobrain_models.items():
            connections[region] = self.create_connection(self.adaptive_neural_network, protobrain_model)
        return connections

    def create_connection(self, adaptive_neural_network, protobrain_model):
        return {
            'input': adaptive_neural_network.get_output_for_region(protobrain_model.region),
            'output': protobrain_model.get_input_from_adaptive_neural_network()
        }

    def update_connection(self, region, adaptive_neural_network, protobrain_model):
        self.connections[region] = self.create_connection(adaptive_neural_network, protobrain_model)

    def process_data_through_connections(self):
        for region, connection in self.connections.items():
            protobrain_input = connection['input']
            connection['output'].send(protobrain_input)
