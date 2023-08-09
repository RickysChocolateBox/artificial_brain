import numpy as np
from collections import defaultdict

class QLearning:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_values = defaultdict(lambda: np.zeros(self.n_actions))

    def choose_action(self, state):
        if np.random.uniform() < self.epsilon:
            return np.random.randint(self.n_actions)
        else:
            return np.argmax(self.q_values[state])

    def update_q_value(self, state, action, next_state, reward):
        old_value = self.q_values[state][action]
        next_max = np.max(self.q_values[next_state])
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
        self.q_values[state][action] = new_value
