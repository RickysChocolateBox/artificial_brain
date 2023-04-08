import numpy as np
import tensorflow as tf

class PolicyGradient:
    def __init__(self, state_size, action_size, learning_rate=0.01, gamma=0.99):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma
        
        self.model = self.build_model()
        self.optimizer = tf.keras.optimizers.Adam(lr=self.learning_rate)
        
        self.states = []
        self.actions = []
        self.rewards = []
        
    def build_model(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(tf.keras.layers.Dense(24, activation='relu'))
        model.add(tf.keras.layers.Dense(self.action_size, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer=self.optimizer)
        return model
        
    def remember(self, state, action, reward):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        
    def act(self, state):
        action_prob = self.model.predict(np.array([state]))
        action = np.random.choice(range(self.action_size), p=action_prob[0])
        return action
        
    def discount_rewards(self, rewards):
        discounted_rewards = np.zeros_like(rewards)
        running_sum = 0
        for i in reversed(range(len(rewards))):
            running_sum = running_sum * self.gamma + rewards[i]
            discounted_rewards[i] = running_sum
        return discounted_rewards
        
    def train(self):
        states = np.array(self.states)
        actions = np.array(self.actions)
        discounted_rewards = self.discount_rewards(self.rewards)
        discounted_rewards -= np.mean(discounted_rewards)
        discounted_rewards /= np.std(discounted_rewards)
        advantages = discounted_rewards
        
        targets = np.zeros((len(states), self.action_size))
        targets[np.arange(len(states)), actions] = 1
        
        self.model.fit(states, targets, sample_weight=advantages, epochs=1, verbose=0)
        
        self.states = []
        self.actions = []
        self.rewards = []

