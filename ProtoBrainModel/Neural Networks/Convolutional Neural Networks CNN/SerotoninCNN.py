import numpy as np
import tensorflow as tf

class SerotoninCNN:
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
        
    def balance_excitation_inhibition(self):
        weights = self.model.get_weights()
        for i in range(0, len(weights), 2):
            mean = (np.mean(weights[i]) + np.mean(weights[i+1])) / 2
            weights[i] = mean * np.ones_like(weights[i])
            weights[i+1] = -mean * np.ones_like(weights[i+1])
        self.model.set_weights(weights)
        
    def train(self, x_train, y_train):
        self.balance_excitation_inhibition()
        self.model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
        self.model.fit(x_train, y_train, epochs=1)

