import numpy as np
import tensorflow as tf

class SimpleRNN(tf.keras.Model):
    def __init__(self, units, input_shape, output_shape):
        super(SimpleRNN, self).__init__()
        self.rnn = tf.keras.layers.SimpleRNN(units, input_shape=input_shape, activation='tanh', return_sequences=True)
        self.dense = tf.keras.layers.Dense(output_shape, activation='linear')

    def call(self, inputs):
        x = self.rnn(inputs)
        x = self.dense(x)
        return x

# Example usage
units = 64
input_shape = (None, 10)
output_shape = 2

model = SimpleRNN(units, input_shape, output_shape)

