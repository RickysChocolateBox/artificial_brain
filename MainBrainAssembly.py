from brainstem import Brainstem
from adaptive_neural_network import AdaptiveNeuralNetwork
from interface import Interface
import os
import shutil

brain_structure_map = {
    'Region1': 'ProtoBrainModel1',
    'Region2': 'ProtoBrainModel2',
    # ... add other regions and their corresponding ProtoBrainModel names
}

# Create instances of Brainstem and AdaptiveNeuralNetwork classes
brainstem = Brainstem()
adaptive_neural_networks = {region: AdaptiveNeuralNetwork(region) for region in brain_structure_map}

# Copy and rename the ProtoBrainModel folders and main files
proto_brain_models = {}
for region, model_name in brain_structure_map.items():
    original_folder = 'ProtoBrainModel'
    new_folder = f'ProtoBrainModel_{model_name}'
    shutil.copytree(original_folder, new_folder)

    original_file = os.path.join(new_folder, 'ProtoBrainModel.py')
    new_file = os.path.join(new_folder, f'{model_name}.py')
    os.rename(original_file, new_file)

    # Import the copied and renamed ProtoBrainModel
    module = __import__(new_folder, fromlist=[model_name])
    model_class = getattr(module, model_name)

    # Create an instance of the copied and renamed ProtoBrainModel
    proto_brain_models[region] = model_class()

# Create an instance of the Interface class
interface = Interface()

# Iterate through the brain_structure_map
for region in brain_structure_map:
    # Get the AdaptiveNeuralNetwork instance corresponding to the current region
    adaptive_nn = adaptive_neural_networks[region]

    # Get the ProtoBrainModel instance corresponding to the current region
    proto_brain_model = proto_brain_models[region]

    # Connect the AdaptiveNeuralNetwork instance with the ProtoBrainModel instance using the Interface
    interface.connect(adaptive_nn, proto_brain_model)

