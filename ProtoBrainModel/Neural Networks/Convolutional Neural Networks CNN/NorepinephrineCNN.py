import tensorflow as tf

class NorepinephrineCNN:
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
        
    def norepinephrine_modulation(self, complexity):
        if complexity > 0:
            self.optimizer.learning_rate = 0.001 + complexity * 0.001
        else:
            self.optimizer.learning_rate = 0.001
        
    def train(self, x_train, y_train, complexity):
        self.norepinephrine_modulation(complexity)
        self.model.compile(optimizer=self.optimizer, loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
        self.model.fit(x_train, y_train, epochs=1)
