import tensorflow as tf

class MLPNetwork(tf.keras.Model):
    def __init__(self, input_shape, hidden_layers, output_shape):
        super(MLPNetwork, self).__init__()
        self.layers_list = []
        self.layers_list.append(tf.keras.layers.InputLayer(input_shape=input_shape))

        for hidden_layer in hidden_layers:
            self.layers_list.append(tf.keras.layers.Dense(hidden_layer, activation='relu'))

        self.layers_list.append(tf.keras.layers.Dense(output_shape, activation='softmax'))

    def call(self, inputs):
        x = inputs
        for layer in self.layers_list:
            x = layer(x)
        return x

# Example usage
input_shape = (10,)  # Number of features
hidden_layers = [64, 32]
output_shape = 2

mlp_network = MLPNetwork(input_shape, hidden_layers, output_shape)
mlp_network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

