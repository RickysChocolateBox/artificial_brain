import tensorflow as tf
from tensorflow import keras 
from keras import layers, models

class Autoencoder:
    def __init__(self, input_shape, encoding_dim, hidden_layers=None, 
                 dopamine_autoencoder=None, gaba_autoencoder=None, 
                 norepinephrine_autoencoder=None, serotonin_autoencoder=None):
        self.input_shape = input_shape
        self.encoding_dim = encoding_dim
        self.hidden_layers = hidden_layers if hidden_layers is not None else [256, 128]
        
        # Include instances of simulated neurotransmitters
        self.dopamine_autoencoder = dopamine_autoencoder
        self.gaba_autoencoder = gaba_autoencoder
        self.norepinephrine_autoencoder = norepinephrine_autoencoder
        self.serotonin_autoencoder = serotonin_autoencoder

        self.encoder = self.build_encoder(input_shape, self.hidden_layers, encoding_dim)
        self.decoder = self.build_decoder(input_shape, self.hidden_layers, encoding_dim)
        self.autoencoder = self.build_autoencoder(input_shape, self.encoder, self.decoder)

    def build_encoder(self, input_shape, hidden_layers, encoding_dim):
        inputs = layers.Input(shape=input_shape)
        x = inputs

        for units in hidden_layers:
            x = layers.Dense(units, activation='relu')(x)
            x = layers.BatchNormalization()(x)
            x = layers.Dropout(0.5)(x)

        encoded = layers.Dense(encoding_dim, activation='relu')(x)
        return models.Model(inputs, encoded, name='encoder')

    def build_decoder(self, input_shape, hidden_layers, encoding_dim):
        inputs = layers.Input(shape=(encoding_dim,))
        x = inputs

        for units in reversed(hidden_layers):
            x = layers.Dense(units, activation='relu')(x)
            x = layers.BatchNormalization()(x)
            x = layers.Dropout(0.5)(x)

        decoded = layers.Dense(input_shape[0], activation='sigmoid')(x)
        return models.Model(inputs, decoded, name='decoder')

    def build_autoencoder(self, input_shape, encoder, decoder):
        inputs = layers.Input(shape=input_shape)
        encoded = encoder(inputs)
        decoded = decoder(encoded)
        return models.Model(inputs, decoded, name='autoencoder')
