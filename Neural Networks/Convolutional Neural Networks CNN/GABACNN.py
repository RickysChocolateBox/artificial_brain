import tensorflow as tf

class GABACNN:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(10)
        ])
        
    def simulate_GABA(self, threshold):
        for i, layer in enumerate(self.model.layers):
            if i == 0:
                continue
            weights = layer.get_weights()
            weights[0][weights[0] < threshold] = 0
            layer.set_weights(weights)
    
    def train(self, x_train, y_train, threshold):
        self.simulate_GABA(threshold)
        self.model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
        self.model.fit(x_train, y_train, epochs=1)

