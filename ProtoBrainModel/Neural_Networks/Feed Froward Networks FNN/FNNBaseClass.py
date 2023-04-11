import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import Dense

class FNN(tf.keras.Model):
    def __init__(self, input_size, output_size, hidden_layers, learning_rate=0.001, neurotransmitter_classes=None):
        super(FNN, self).__init__()

        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.neurotransmitter_classes = neurotransmitter_classes if neurotransmitter_classes is not None else []

        self.model = tf.keras.Sequential()
        for hidden_layer in hidden_layers:
            self.model.add(Dense(hidden_layer, activation='relu'))
        self.model.add(Dense(output_size, activation='linear'))

        self.optimizer = tf.keras.optimizers.Adam(lr=learning_rate)
        self.loss_object = tf.keras.losses.MeanSquaredError()

    def call(self, inputs):
        return self.model(inputs)

    def update_neurotransmitter_levels(self, toolkit_report):
        for neurotransmitter_class in self.neurotransmitter_classes:
            neurotransmitter = neurotransmitter_class()

            if hasattr(neurotransmitter, 'learning_rate'):
                keras.backend.set_value(self.optimizer.lr, neurotransmitter.learning_rate)

    def train_step(self, inputs, targets):
        with tf.GradientTape() as tape:
            predictions = self.model(inputs)
            loss = self.loss_object(targets, predictions)

        gradients = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))

        return loss.numpy()
