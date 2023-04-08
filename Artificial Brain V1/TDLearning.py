import numpy as np

class TDLearning:
    def __init__(self, learning_rate, discount_factor):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.Q_table = {}

    def update(self, state, action, reward, next_state):
        if state not in self.Q_table:
            self.Q_table[state] = np.zeros(action.shape)
        
        if next_state not in self.Q_table:
            self.Q_table[next_state] = np.zeros(action.shape)
        
        td_error = reward + self.discount_factor * np.max(self.Q_table[next_state]) - self.Q_table[state][action]
        self.Q_table[state][action] += self.learning_rate * td_error

    def choose_action(self, state, actions):
        if state not in self.Q_table:
            self.Q_table[state] = np.zeros(len(actions))
        
        if np.random.rand() < self.epsilon:
            return np.random.choice(actions)
        else:
            return np.argmax(self.Q_table[state])

