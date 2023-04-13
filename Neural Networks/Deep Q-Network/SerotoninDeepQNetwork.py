import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers 
from keras import Dense

class Serotonin(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(Serotonin, self).__init__(**kwargs)
        
    def call(self, inputs):
        # Maintain a balance between excitatory and inhibitory neurons in
        # the network to promote stable reinforcement learning and action
        # selection.
        return tf.nn.tanh(inputs)

