
import tensorflow as tf

class NorepinephrineAutoencoder:
    def __init__(self, input_dim, encoding_dim):
        self.input_dim = input_dim
        self.encoding_dim = encoding_dim
        self.encoder = tf.keras.Sequential([
            tf.keras.layers.Dense(256, activation='relu', input_shape=(input_dim,)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(encoding_dim, activation='relu'),
        ])
        self.decoder = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(encoding_dim,)),
            tf.keras.layers.Dense(256, activation='relu'),
            tf.keras.layers.Dense(input_dim, activation='sigmoid'),
        ])
        self.autoencoder = tf.keras.Sequential([self.encoder, self.decoder])
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)

    def train(self, x_train, x_test, epochs=10, batch_size=32):
        self.autoencoder.compile(optimizer=self.optimizer, loss='mse')
        self.autoencoder.fit(x_train, x_train, epochs=epochs, batch_size=batch_size, shuffle=True, validation_data=(x_test, x_test))
        
    def encode(self, x):
        return self.encoder.predict(x)

    def decode(self, x):
        return self.decoder.predict(x)
