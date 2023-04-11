import numpy as np
import DopamineANN
import GABANN
import NorepinephrineANN
import SerotoninANN

class ANNBaseClass:
    def __init__(self, input_dim, hidden_dim, output_dim, learning_rate=0.01):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.learning_rate = learning_rate
        self.weights_input_to_hidden = np.random.randn(input_dim, hidden_dim)
        self.weights_hidden_to_output = np.random.randn(hidden_dim, output_dim)

        # Initialize neurotransmitter models
        self.dopamine = DopamineANN(learning_rate)
        self.gaba = GABANN(input_dim, output_dim)
        self.norepinephrine = NorepinephrineANN(learning_rate)
        self.serotonin = SerotoninANN(learning_rate)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def update_neurotransmitter_levels(self, toolkit_report):
        # Update neurotransmitter levels based on the toolkit report
        dopamine_level = toolkit_report['dopamine']
        gaba_level = toolkit_report['gaba']
        norepinephrine_level = toolkit_report['norepinephrine']
        serotonin_level = toolkit_report['serotonin']

        self.dopamine.learning_rate = dopamine_level
        self.gaba.weights *= gaba_level
        self.norepinephrine.learning_rate = norepinephrine_level
        self.serotonin.weights *= serotonin_level

    def forward(self, X):
        self.layer0 = X
        self.layer1 = self.sigmoid(np.dot(self.layer0, self.weights_input_to_hidden))
        self.layer2 = self.sigmoid(np.dot(self.layer1, self.weights_hidden_to_output))
        return self.layer2

    def backward(self, X, y, output):
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoid_derivative(output)
        
        self.layer1_error = self.output_delta.dot(self.weights_hidden_to_output.T)
        self.layer1_delta = self.layer1_error * self.sigmoid_derivative(self.layer1)

        self.weights_hidden_to_output += self.layer1.T.dot(self.output_delta) * self.learning_rate
        self.weights_input_to_hidden += self.layer0.T.dot(self.layer1_delta) * self.learning_rate

    def train(self, X, y):
        output = self.forward(X)
        self.backward(X, y, output)

    def predict(self, X):
        return self.forward(X)

    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate

