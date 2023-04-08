import tensorflow as tf

class LSTMNetwork(tf.keras.Model):
    def __init__(self, input_shape, num_units, output_shape):
        super(LSTMNetwork, self).__init__()
        self.lstm = tf.keras.layers.LSTM(num_units, input_shape=input_shape, return_sequences=True)
        self.output_layer = tf.keras.layers.Dense(output_shape, activation='softmax')

    def call(self, inputs):
        lstm_output = self.lstm(inputs)
        output = self.output_layer(lstm_output)
        return output

# Example usage
input_shape = (None, 10)  # Sequence length, number of features
num_units = 128
output_shape = 2

lstm_network = LSTMNetwork(input_shape, num_units, output_shape)
lstm_network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

