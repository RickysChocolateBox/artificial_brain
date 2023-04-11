import tensorflow as tf

class DopamineCNN:
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
        self.optimizer = tf.keras.optimizers.Adam()
        
    def dopamine_release(self, reward):
        if reward > 0:
            self.optimizer.learning_rate = 0.001 + reward * 0.001
        else:
            self.optimizer.learning_rate = 0.001
        
    def train(self, x_train, y_train, reward):
        self.dopamine_release(reward)
        self.model.compile(optimizer=self.optimizer, loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
        self.model.fit(x_train, y_train, epochs=1)
