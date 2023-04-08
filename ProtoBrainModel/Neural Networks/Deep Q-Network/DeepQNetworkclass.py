import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense

class DQN(tf.keras.Model):
    def __init__(self, state_size, action_size, hidden_layers, learning_rate=0.001):
        super(DQN, self).__init__()

        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate

        self.model = tf.keras.Sequential()
        for hidden_layer in hidden_layers:
            self.model.add(Dense(hidden_layer, activation='relu'))
        self.model.add(Dense(action_size, activation='linear'))

        self.optimizer = tf.keras.optimizers.Adam(lr=learning_rate)

    def call(self, state):
        return self.model(state)

    def train_step(self, states, actions, rewards, next_states, dones, gamma=0.99):
        with tf.GradientTape() as tape:
            q_values = self.model(states)
            one_hot_actions = tf.keras.utils.to_categorical(actions, self.action_size, dtype=np.float32)
            q_values = tf.reduce_sum(tf.multiply(q_values, one_hot_actions), axis=1)

            next_q_values = self.model(next_states)
            next_q_values = tf.stop_gradient(next_q_values)

            max_next_q_values = tf.reduce_max(next_q_values, axis=1)
            target_q_values = rewards + (1 - dones) * gamma * max_next_q_values

            loss = tf.keras.losses.MSE(target_q_values, q_values)

        grads = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

        return loss.numpy()
