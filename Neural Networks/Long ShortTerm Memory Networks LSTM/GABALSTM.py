import tensorflow as tf

class GABALSTM(tf.keras.Model):
    def __init__(self, **kwargs):
        super(GABALSTM, self).__init__(**kwargs)
        self.lstm_layer = tf.keras.layers.LSTM(units=64, return_sequences=True, activation='tanh', recurrent_activation='sigmoid', recurrent_dropout=0.5)
        self.dense_layer = tf.keras.layers.Dense(units=1, activation='sigmoid')

    def call(self, inputs, training=None, mask=None):
        x = self.lstm_layer(inputs)
        x = self.dense_layer(x)
        return x


