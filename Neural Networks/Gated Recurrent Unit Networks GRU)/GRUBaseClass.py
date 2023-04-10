import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import GRU, Dense

class GRUNetwork(tf.keras.Model):
    def __init__(self, input_size, output_size, hidden_size, num_layers, learning_rate=0.001, neurotransmitter_classes=None):
        super(GRUNetwork, self).__init__()

        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.learning_rate = learning_rate
        self.neurotransmitter_classes = neurotransmitter_classes if neurotransmitter_classes is not None else []

        self.gru = GRU(hidden_size, return_sequences=True, return_state=True, num_layers=num_layers)
        self.fc = Dense(output_size)

        self.optimizer = tf.keras.optimizers.Adam(lr=learning_rate)
        self.loss_object = tf.keras.losses.MeanSquaredError()

    def call(self, inputs, hidden):
        output, hidden_state = self.gru(inputs, initial_state=hidden)
        output = self.fc(output)
        return output, hidden_state

    def update_neurotransmitter_levels(self, toolkit_report):
        for neurotransmitter_class in self.neurotransmitter_classes:
            neurotransmitter = neurotransmitter_class()

            if hasattr(neurotransmitter, 'learning_rate'):
                keras.backend.set_value(self.optimizer.lr, neurotransmitter.learning_rate)

    def train_step(self, inputs, targets, hidden):
        with tf.GradientTape() as tape:
            predictions, _ = self.call(inputs, hidden)
            loss = self.loss_object(targets, predictions)

        gradients = tape.gradient(loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))

        return loss.numpy()

