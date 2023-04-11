import tensorflow as tf

class GABALayer(tf.keras.layers.Layer):
    def __init__(self, connection_strength, **kwargs):
        super(GABALayer, self).__init__(**kwargs)
        self.connection_strength = connection_strength
        
    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel',
                                      shape=(input_shape[-1], input_shape[-1]),
                                      initializer='glorot_uniform',
                                      trainable=True)
        super(GABALayer, self).build(input_shape)
        
    def call(self, inputs):
        # Apply the GABA effect by weakening specific connections
        inputs = tf.multiply(inputs, self.kernel * self.connection_strength)
        return inputs

