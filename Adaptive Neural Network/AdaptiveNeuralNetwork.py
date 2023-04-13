import sys
sys.path.append("sys:\Users\info\anaconda3\envs\Artificial_Brain_Project\Lib\site-packages")
import sys
sys.path.append("sys:\Users\info\OneDrive\Desktop\Artificia Brain\artificial_brain\ProtoBrainModel\ProtoBrainModel.py")
import random
import tensorflow as tf
import networkx as nx
import gym 
import numpy as np 
from ProtoBrainModel import ProtoBrainModel 
from deap import algorithms, base, creator, tools
from emotional_class import EmotionalModel
from NeurotransmitterTuner import NeurotransmitterTuner
from AutoTuneToolkit import AutoTuneToolkit  

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
class AdaptiveNeuralNetwork:
    def __init__(self, num_neurons, learning_rate, num_emotions=5):
        self.neurons = [Neuron() for _ in range(num_neurons)]
        self.learning_rate = learning_rate
        self.hebbian_learning = HebbianLearning()
        self.synaptic_scaling = SynapticScaling()
        self.emotional_model = EmotionalModel(num_emotions=num_emotions)
        self, num_neurons, learning_rate
        self.neurons = [Neuron() for _ in range(num_neurons)]
        self.brain_structure = self.load_brain_structure()
        self.neurotransmitter_tuner = NeurotransmitterTuner(self)
        self.brain_structure = self.load_brain_structure()
    def receive_toolkit_report(self, toolkit, action_data):
        # Process the report from the toolkit
        # This can involve updating internal data structures, making decisions, etc.
        pass

    def create_toolkits(self, num_toolkits, reinforcement_learning_models):
        for _ in range(num_toolkits):
            toolkit = AutoTuneToolkit(self, reinforcement_learning_models)
            self.toolkits.append(toolkit)

    def create_and_optimize_proto_brain_model(self, brain_structure_map, sensory_data, state_size, action_size, learning_rate, discount_factor, exploration_rate):
        proto_brain_model = ProtoBrainModel(brain_structure_map, sensory_data, state_size, action_size, learning_rate, discount_factor, exploration_rate)
        toolkit = AutoTuneToolkit(self)
        proto_brain_model.optimize_components(toolkit)
        return proto_brain_model

    def load_brain_structure(self):
        brain_structure = {
    "Left Hemisphere": {
        "Forebrain": {
            "Telencephalon": {
                "Cerebral_cortex": {
                    "Neocortex": {
                        "Frontal_lobe": {},
                        "Parietal_lobe": {},
                        "Temporal_lobe": {},
                        "Occipital_lobe": {}
                    },
                    "Paleocortex": {
                        "Olfactory_cortex": {}
                    },
                    "Archicortex": {
                        "Hippocampus": {}
                    },
                    "Other_cortical_regions": {
                        "Prefrontal_cortex": {},
                        "Insular_cortex": {},
                        "Cingulate_cortex": {},
                    }
                },
                "Basal_ganglia": {
                    "Striatum": {
                        "Caudate_nucleus": {},
                        "Putamen": {},
                    },
                    "Globus_pallidus": {
                        "External_globus_pallidus": {},
                        "Internal_globus_pallidus": {},
                    },
                    "Subthalamic_nucleus": {},
                    "Substantia_nigra": {},
                },
                "Limbic_system": {
                    "Amygdala": {},
                    "Hippocampus": {},
                    "Fornix": {},
                    "Mammillary_body": {},
                    "Septal_nuclei": {},
                    "Cingulate_gyrus": {},
                    "Parahippocampal_gyrus": {},
                },
            },
            "Diencephalon": {
                "Thalamus": {},
                "Hypothalamus": {
                    "Supraoptic_nucleus": {},
                    "Paraventricular_nucleus": {},
                    "Anterior_hypothalamic_nucleus": {},
                    "Ventromedial_nucleus": {},
                    "Arcuate_nucleus": {},
                    "Lateral_hypothalamic_area": {},
                },
                "Epithalamus": {
                    "Pineal_gland": {},
                    "Habenula": {},
                },
                "Subthalamus": {
                    "Subthalamic_nucleus": {},
                },
            },
        },
        "Midbrain": {
            "Tectum": {
                "Superior_colliculus": {},
                "Inferior_colliculus": {},
            },
            "Tegmentum": {
                "Periaqueductal_gray": {},
                "Reticular_formation": {},
                "Red_nucleus": {},
                "Substantia_nigra": {},
            },
            "Cerebral_penduncle": {
                "Crus_cerebri": {},
            },
        },
        "Hindbrain": {
            "Metencephalon": {
                "Pons": {},
                "Cerebellum": {
                    "Cerebellar_cortex": {
                        "Anterior_lobe": {},
                        "Posterior_lobe": {},
                        "Flocculonodular_lobe": {},
                    },
                    "Cerebellar_nuclei": {
                        "Dentate_nucleus": {},
                        "Interposed_nucleus": {},
                        "Fastigial_nucleus": {},
                    },
                },
            },
            "Myelencephalon": {
                "Medulla_oblongata": {
                    "Pyramids": {},
                    "Olive": {},
                    "Reticular_formation": {},
                    "Cranial_nerve_nuclei": {},
                },
            },
        },
    },
    "Right Hemisphere": {
         "Forebrain": {
            "Telencephalon": {
                "Cerebral_cortex": {
                    "Neocortex": {
                        "Frontal_lobe": {},
                        "Parietal_lobe": {},
                        "Temporal_lobe": {},
                        "Occipital_lobe": {}
                    },
                    "Paleocortex": {
                        "Olfactory_cortex": {}
                    },
                    "Archicortex": {
                        "Hippocampus": {}
                    },
                    "Other_cortical_regions": {
                        "Prefrontal_cortex": {},
                        "Insular_cortex": {},
                        "Cingulate_cortex": {},
                    }
                },
                "Basal_ganglia": {
                    "Striatum": {
                        "Caudate_nucleus": {},
                        "Putamen": {},
                    },
                    "Globus_pallidus": {
                        "External_globus_pallidus": {},
                        "Internal_globus_pallidus": {},
                    },
                    "Subthalamic_nucleus": {},
                    "Substantia_nigra": {},
                },
                "Limbic_system": {
                    "Amygdala": {},
                    "Hippocampus": {},
                    "Fornix": {},
                    "Mammillary_body": {},
                    "Septal_nuclei": {},
                    "Cingulate_gyrus": {},
                    "Parahippocampal_gyrus": {},
                },
            },
            "Diencephalon": {
                "Thalamus": {},
                "Hypothalamus": {
                    "Supraoptic_nucleus": {},
                    "Paraventricular_nucleus": {},
                    "Anterior_hypothalamic_nucleus": {},
                    "Ventromedial_nucleus": {},
                    "Arcuate_nucleus": {},
                    "Lateral_hypothalamic_area": {},
                },
                "Epithalamus": {
                    "Pineal_gland": {},
                    "Habenula": {},
                },
                "Subthalamus": {
                    "Subthalamic_nucleus": {},
                },
            },
        },
        "Midbrain": {
            "Tectum": {
                "Superior_colliculus": {},
                "Inferior_colliculus": {},
            },
            "Tegmentum": {
                "Periaqueductal_gray": {},
                "Reticular_formation": {},
                "Red_nucleus": {},
                "Substantia_nigra": {},
            },
            "Cerebral_penduncle": {
                "Crus_cerebri": {},
            },
        },
        "Hindbrain": {
            "Metencephalon": {
                "Pons": {},
                "Cerebellum": {
                    "Cerebellar_cortex": {
                        "Anterior_lobe": {},
                        "Posterior_lobe": {},
                        "Flocculonodular_lobe": {},
                    },
                    "Cerebellar_nuclei": {
                        "Dentate_nucleus": {},
                        "Interposed_nucleus": {},
                        "Fastigial_nucleus": {},
                    },
                },
            },
            "Myelencephalon": {
                "Medulla_oblongata": {
                    "Pyramids": {},
                    "Olive": {},
                    "Reticular_formation": {},
                    "Cranial_nerve_nuclei": {},
                },
            },
        },
    },
} 

        return brain_structure
    def fractal_growth_pattern(self, input_data, target_data, num_generations=50, population_size=100):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        toolbox = base.Toolbox()
        toolbox.register("attr_bool", np.random.choice, [0, 1])
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=len(self.neurons))
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("select", tools.selBest)
        toolbox.register("evaluate", self.evaluate_growth_pattern, input_data=input_data, target_data=target_data)

        population = toolbox.population(n=population_size)

        algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=num_generations, verbose=False)

        best_individual = tools.selBest(population, k=1)[0]
        self.apply_growth_pattern(best_individual)

    def evaluate_growth_pattern(self, individual, input_data, target_data):
        # Implement logic to evaluate the performance of the network with the proposed growth pattern
        pass

    def apply_growth_pattern(self, growth_pattern):
        # Implement logic to apply the growth pattern (new neurons and connections) to the network
        pass
    def process_input_data(self, input_data):
        for neuron in self.neurons:
            neuron.process_inputs(input_data)

        self.hebbian_learning.update_weights(self.neurons, self.learning_rate)
        self.synaptic_scaling.scale_synapses(self.neurons)
    def forward_pass(self, input_values):
        # Apply the emotional influence
        influenced_values = self.emotional_model.get_emotional_influence(input_values)

        # Replace input_values with influenced_values in the forward pass
        output_values = self.layers[0].forward(influenced_values)

        for i in range(1, len(self.layers)):
            output_values = self.layers[i].forward(output_values)

        return output_values

def load_training_data():
    # Replace with your actual dataset
    X_train = np.random.rand(100, 10)
    y_train = np.random.randint(0,)
    y_train = np.random.randint(0, 2, size=(100,))
    return X_train, y_train

def load_test_data():
    # Replace with your actual dataset
    X_test = np.random.rand(50, 10)
    y_test = np.random.randint(0, 2, size=(50,))
    return X_test, y_test

def evaluate_performance(y_true, y_pred):
    assert len(y_true) == len(y_pred), "Lengths of true and predicted values must be the same."
    correct_predictions = sum(y1 == y2 for y1, y2 in zip(y_true, y_pred))
    accuracy = correct_predictions / len(y_true)
    return accuracy

def main():
    # Create an instance of the AdaptiveNeuralNetwork with 10 neurons, learning rate of 0.01, and 5 emotions
    ann = AdaptiveNeuralNetwork(num_neurons=10, learning_rate=0.01, num_emotions=5)

    # Load the dataset for training
    X_train, y_train = load_training_data()

    # Train the AdaptiveNeuralNetwork
    ann.train(X_train, y_train)

    # Load the dataset for testing
    X_test, y_test = load_test_data()

    # Make predictions using the trained AdaptiveNeuralNetwork
    y_pred = ann.predict(X_test)

    # Evaluate the performance of the AdaptiveNeuralNetwork
    accuracy = evaluate_performance(y_test, y_pred)

    print("Accuracy of the AdaptiveNeuralNetwork:", accuracy)

    # Example of updating the emotional state
    ann.emotional_model.increase_emotion(emotion_index=0, value=0.2)  # Increase the first emotion by 0.2
    ann.emotional_model.decay_emotions()  # Decay the emotions

    # Make predictions with the updated emotional state
    y_pred_updated = ann.predict(X_test)

    # Evaluate the performance of the AdaptiveNeuralNetwork with the updated emotional state
    accuracy_updated = evaluate_performance(y_test, y_pred_updated)

    print("Accuracy of the AdaptiveNeuralNetwork with updated emotional state:", accuracy_updated)

# Call the main function
if __name__ == "__main__":
    main()

def main():
    adaptive_nn = AdaptiveNeuralNetwork(num_neurons=10, learning_rate=0.01)

    # Example usage:
    inputs = np.array([1, 2, 3])
    for neuron in AdaptiveNeuralNetwork.neurons:
        outputs = neuron.process_inputs(inputs)
        print(outputs)


if __name__ == "__main__":
    main()
