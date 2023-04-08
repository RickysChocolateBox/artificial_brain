import tensorflow as tf
from tensorflow.keras.layers import Dense

class FNN(tf.keras.Model):
    def __init__(self, input_size, output_size, hidden_layers, learning_rate=0.001):
        super(FNN, self).__init__()

        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        self.model = tf.keras.Sequential()
        for hidden_layer in hidden_layers:
            self.model.add(Dense(hidden_layer, activation='relu'))
        self.model.add(Dense(output_size, activation='linear'))

        self.optimizer = tf.keras.optimizers.Adam(lr=learning_rate)
        self.loss_object = tf.keras.losses.MeanSquaredError()

    def call(self, inputs):
        return self.model(inputs)

    def train_step(self, inputs, targets):
        with tf.GradientTape() as tape:
            predictions = self.model(inputs)
            loss = self.loss_object(targets, predictions)

        gradients = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))

        return loss.numpy()


