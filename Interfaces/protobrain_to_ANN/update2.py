class Interface:
    def __init__(self, proto_brain, adaptive_nn):
        self.proto_brain = proto_brain
        self.adaptive_nn = adaptive_nn

    def process_sensory_data(self, sensory_data):
        # First, pass the sensory data to the Proto-brain model.
        processed_data, labels = self.proto_brain.process_sensory_data(sensory_data)

        # Then, pass the processed data and labels to the Adaptive Neural Network for further processing.
        self.adaptive_nn.train_model(processed_data, labels)

    def control_output(self):
        # Get the output from the Adaptive Neural Network.
        output = self.adaptive_nn.get_output()

        # Based on the output, apply your control logic.
        # Replace the example logic with your own implementation.
        control_signal = output * 100

        return control_signal


# Example usage:
brain_region = "vision"
sensory_data = np.random.rand(100, 28, 28)  # Replace this with the actual sensory data.

proto_brain = ProtoBrainModel(brain_region, sensory_data)
adaptive_nn = AdaptiveNeuralNetwork()

interface = Interface(proto_brain, adaptive_nn)

# Train the models
interface.process_sensory_data(sensory_data)

# Get control signals
control_signal = interface.control_output()

