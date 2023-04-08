
import tensorflow as tf

class SerotoninAutoencoder:
    def __init__(self, input_dim, encoding_dim):
        self.input_dim = input_dim
        self.encoding_dim = encoding_dim
        self.encoder = tf.keras.Sequential([
            tf.keras.layers.Dense(256, activation='tanh', input_shape=(input_dim,)),
            tf.keras.layers.Dense(128, activation='tanh'),
            tf.keras.layers.Dense(encoding_dim, activation='tanh'),
        ])
        self.decoder = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='tanh', input_shape=(encoding_dim,)),
            tf.keras.layers.Dense(256, activation='tanh'),
            tf.keras.layers.Dense(input_dim, activation='sigmoid'),
        ])
        self.autoencoder = tf.keras.Sequential([self.encoder, self.decoder])
