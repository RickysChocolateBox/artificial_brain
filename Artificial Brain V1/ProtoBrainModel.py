import sys
sys.path.append("C:\\Users\\info\\HebbianLearningThesis\\HebbianLearningThesis")
import numpy as np
import random
import math
from FractalGrowthPattern import FractalGrowthPattern
from GeneticAlgorithm import GeneticAlgorithm
from ReinforcementLearningClass import ReinforcementLearning
from CorrectionMechanisms import CorrectionMechanism
from RandomParameterGenerator import RandomParameterGenerator
from IntrinsicMotivationQAgent import IntrinsicMotivationQAgent
from AutoTuneToolkit import AutoTuneToolkit  
from AutoTuneToolkit import NeurotransmitterTuner
from ANNBaseClass import ANN
from AE_BaseClass import Autoencoder
from BoltzmannMachineclass import RBM
from CNNBaseClass import CNN
from DBNBaseClass import DBN
from DeepQNetworkBaseClass import DQN
from FNNBaseClass import FNN
from GRUBaseClass import GRUNetwork
from HopfieldBaseClass import HopfieldNetwork
from LSNNBaseClass import LSNN
from LSTMBaseClass import LSTMNetwork
from MLPBaseClass import MLPNetwork
from RBFNBaseClass import RBFN
from RNNBaseClass import SimpleRNN
from SOMBaseClass import SOM
from VAEBaseClass import VAE

class HebbianLearning:
    def update_weights(self, neurons, learning_rate):
        for neuron in neurons:
            for synapse in neuron.synapses:
                # Update the synapse weight based on the Hebbian learning rule
                synapse.weight += learning_rate * neuron.activation * synapse.target.activation
        pass


class SynapticScaling:
    def scale_synapses(self, neurons, target_sum):
        for neuron in neurons:
            synapse_weights = [synapse.weight for synapse in neuron.synapses]
            sum_weights = sum(synapse_weights)

            if sum_weights > 0:
                scale_factor = target_sum / sum_weights
                for synapse in neuron.synapses:
                    synapse.weight *= scale_factor
        pass

class Neuron:
    def process_inputs(self, inputs):
        attention_weights = self.calculate_attention_weights(inputs)
        attended_inputs = self.apply_attention(inputs, attention_weights)
        processed_outputs = self.process_attended_inputs(attended_inputs)
        return processed_outputs
    def request_neurotransmitter_adjustment(self, proto_brain_model, adjustment_type):
        return self.neurotransmitter_tuner.adjust_neurotransmitters(proto_brain_model, adjustment_type)

    def calculate_attention_weights(self, inputs):
        attention_weights = [1.0 / len(inputs) for _ in range(len(inputs))]
        return attention_weights

    def apply_attention(self, inputs, attention_weights):
        attended_inputs = inputs * attention_weights
        return attended_inputs

    def process_attended_inputs(self, attended_inputs):
        processed_outputs = attended_inputs * 2
        return processed_outputs

    def report_action(self, action_data):
        self.ann.receive_toolkit_report(self, action_data)

class ProtoBrainModel:
    def __init__(self, brain_structure_map, sensory_data, state_size, action_size, learning_rate, discount_factor, exploration_rate):
        self.brain_structure_map = brain_structure_map
        self.sensory_data = sensory_data
        self.network_types = ["ANN", "Autoencoder", "RBM", "CNN", "DBN", "DQN", "FNN", "GRUNetwork", "HopfieldNetwork", "LSNN", "LSTMNetwork", "MLPNetwork", "RBFN","SimpleRNN","SOM","VAE",
        ]
        self.neural_networks = self.initialize_neural_networks()
        self.genetic_algorithm = GeneticAlgorithm()
        self.reinforcement_learning = ReinforcementLearning()
        self.correction_mechanism = CorrectionMechanism()
        self.intrinsic_motivation_agent = IntrinsicMotivationQAgent(state_size, action_size, learning_rate, discount_factor, exploration_rate)
        self.autotune_toolkit = AutoTuneToolkit()  # Initialize AutotuneToolkit

    def initialize_neural_networks(self):
        neural_networks = {}
        for region, network_type in self.brain_structure_map.items():
            if network_type in self.network_types:
                neural_networks[region] = self.create_network(network_type)
            else:
                raise ValueError(f"Invalid network type specified: {network_type}")
        return neural_networks

    def create_network(self, network_type):
        if network_type == "":
            return ()

        else:
            # Use the AutotuneToolkit to find the best network type for the given region
            best_network_type = self.autotune_toolkit.find_best_network_type(self.sensory_data, self.network_types)
        
        if best_network_type == "ANN":
            return ANN()
        elif best_network_type == "Autoencoder":
            return Autoencoder()
        elif best_network_type == "RBM":
            return RBM()
        elif best_network_type == "CNN":
            return CNN()
        elif best_network_type == "DBN":
            return DBN()
        elif best_network_type == "DQN":
            return DQN()
        elif best_network_type == "FNN":
            return FNN()
        elif best_network_type == "GRUNetwork":
            return GRUNetwork()
        elif best_network_type == "HopfieldNetwork":
            return HopfieldNetwork()
        elif best_network_type == "LSNN":
            return LSNN()
        elif best_network_type == "LSTMNetwork":
            return LSTMNetwork()
        elif best_network_type == "MLPNetwork":
            return MLPNetwork()
        elif best_network_type == "RBFN":
            return RBFN()
        elif best_network_type == "SimpleRNN":
            return SimpleRNN()
        elif best_network_type == "SOM":
            return SOM()
        elif best_network_type == "VAE":
            return VAE()
        else:
            raise ValueError(f"Invalid network type: {best_network_type}")

    def process_sensory_data(self):
        reprocessed_data = {}
        for region, network in self.neural_networks.items():
            reprocessed_data[region] = network.process(self.sensory_data[region])
        return reprocessed_data

    def select_optimal_network(self, reprocessed_data):
        self.genetic_algorithm.select_best_individuals(reprocessed_data)
        self.reinforcement_learning.update(reprocessed_data)

    def apply_correction_mechanism(self):
        self.correction_mechanism.correct_overfitting(self.neural_networks)

    def train(self):
        self.training_complete = False
        while not self.training_complete:
            sensory_data = self.receive_sensory_data()
            self.sensory_data = self.process_sensory_data()

            # Update the brain structure map and the neural networks
            self.update_brain_structure_map()
            self.update_neural_networks()

            # Train the neural networks using the selected network types
            for region, network in self.neural_networks.items():
                input_data, target_data = self.prepare_training_data(self.sensory_data[region])

                # Select the best optimization algorithm using the AutotuneToolkit
                best_algorithm = self.autotune_toolkit.select_best_algorithm(network, input_data, target_data)

                # Optimize hyperparameters using the selected optimization algorithm
                self.autotune_toolkit.optimize(network, input_data, target_data, best_algorithm)

                # Train the neural network with optimized hyperparameters
                network.train(input_data, target_data)

            # Evaluate the performance of the neural networks
            performance = self.evaluate_performance()

            # Select the optimal network configuration based on the performance
            self.select_optimal_network(performance)

            # Apply the correction mechanism if necessary
            if self.detect_mistake() or self.detect_overfitting():
                self.apply_correction_mechanism()

            # Update the training progress and check if the training is complete
            self.update_training_progress()
            self.training_complete = self.check_training_complete()

    def receive_sensory_data(self, adaptive_neural_network):
    # Get sensory data from the Adaptive Neural Network
        sensory_data = adaptive_neural_network.get_sensory_data_for_protobrain()
        return sensory_data

    def update_brain_structure_map(self, learning_experience):
        # Process learning experiences from the simulation and extract relevant information
        processed_experience = self.process_learning_experience(learning_experience)
        
        # Update the brain structure map based on the processed learning experience
        self.brain_structure_map.update(processed_experience)

    def update_neural_networks(self):
        # Iterate through the Protobrain models in the brain structure map
        for region, protobrain_model in self.brain_structure_map.items():
            # Retrieve the specific information for the current Protobrain model
            model_information = self.get_model_information(region)

            # Update the current Protobrain model based on the retrieved information
            protobrain_model.update(model_information)

            # Use the auto tune tool kit to evaluate the performance of the Protobrain model
            self.auto_tune_toolkit.evaluate_performance(protobrain_model)

    def evaluate_performance(self):
        performance_scores = self.autotune_toolkit.evaluate_neural_network_performance(self.neural_networks, self.sensory_data)
        return performance_scores

    def detect_mistake(self):
        mistake_detected = self.autotune_toolkit.detect_mistake(self.neural_networks, self.sensory_data)
        return mistake_detected

    def detect_overfitting(self):
        overfitting_detected = self.autotune_toolkit.detect_overfitting(self.neural_networks, self.sensory_data)
        return overfitting_detected

    def update_training_progress(self):
        # Iterate through the Protobrain models in the brain structure map
        for region, protobrain_model in self.brain_structure_map.items():
            # Retrieve the specific information for the current Protobrain model
            model_information = self.get_model_information(region)

            # Update the current Protobrain model based on the retrieved information
            protobrain_model.update(model_information)

            # Evaluate the training progress of the Protobrain model using the AutoTuneToolkit
            progress = self.auto_tune_toolkit.assess_training_progress(protobrain_model)

            # Update the training progress for the current Protobrain model
            protobrain_model.training_progress = progress

    def check_training_complete(self):
        training_complete = self.autotune_toolkit.check_training_complete(self.neural_networks, self.sensory_data)
        return training_complete

