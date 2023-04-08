import tensorflow as tf

class SerotoninRNN:
    def __init__(self, hidden_units):
        self.model = tf.keras.Sequential([
            tf.keras.layers.SimpleRNN(hidden_units, activation='relu', return_sequences=True),
            tf.keras.layers.Dense(1)
        ])
        self.optimizer = tf.keras.optimizers.Adam()
        self.hidden_units = hidden_units
        
    def balance_excitation_inhibition(self):
        self.model.layers[0].activation = 'tanh'
        
    def train(self, x_train, y_train):
        self.balance_excitation_inhibition()
        self.model.compile(optimizer=self.optimizer, loss='mse')
        self.model.fit(x_train, y_train, epochs=1)
