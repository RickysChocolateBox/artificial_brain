import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

class LSNN:
    def __init__(self, input_shape, reservoir_size, output_size, connectivity=0.1, spectral_radius=0.9):
        self.input_shape = input_shape
        self.reservoir_size = reservoir_size
        self.output_size = output_size
        self.connectivity = connectivity
        self.spectral_radius = spectral_radius
        self.lsnn = self.build_lsnn(input_shape, reservoir_size, output_size)

    def build_lsnn(self, input_shape, reservoir_size, output_size):
        inputs = layers.Input(shape=input_shape)

        # Initialize reservoir weights
        reservoir_weights = np.random.rand(reservoir_size, reservoir_size) - 0.5
        reservoir_weights = (np.random.rand(reservoir_size, reservoir_size) < self.connectivity) * reservoir_weights
        reservoir_eigenvalues = np.linalg.eigvals(reservoir_weights)
        reservoir_weights *= self.spectral_radius / np.max(np.abs(reservoir_eigenvalues))

        # Reservoir layer
        reservoir = layers.Dense(reservoir_size, activation='tanh', trainable=False, kernel_initializer=tf.keras.initializers.Constant(reservoir_weights))(inputs)

        # Readout layer
        readout = layers.Dense(output_size, activation='linear')(reservoir)

        return models.Model(inputs, readout, name='lsnn')


