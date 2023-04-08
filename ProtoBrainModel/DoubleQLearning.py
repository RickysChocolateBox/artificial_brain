import numpy as np
import random

class DoubleQLearning:
    def __init__(self, alpha, gamma, epsilon, actions):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions
        self.Q1 = {}
        self.Q2 = {}
        self.reset()

    def reset(self):
        self.Q1 = {}
        self.Q2 = {}

    def update(self, state, action, reward, next_state, done):
        if state not in self.Q1:
            self.Q1[state] = {a: 0.0 for a in self.actions}
            self.Q2[state] = {a: 0.0 for a in self.actions}
        if next_state not in self.Q1:
            self.Q1[next_state] = {a: 0.0 for a in self.actions}
            self.Q2[next_state] = {a: 0.0 for a in self.actions}

        if random.uniform(0, 1) < 0.5:
            self.update_q(self.Q1, self.Q2, state, action, reward, next_state, done)
        else:
            self.update_q(self.Q2, self.Q1, state, action, reward, next_state, done)

    def update_q(self, Q1, Q2, state, action, reward, next_state, done):
        if done:
            Q1[state][action] += self.alpha * (reward - Q1[state][action])
        else:
            max_next_action = max(Q1[next_state], key=Q1[next_state].get)
            Q1[state][action] += self.alpha * (reward + self.gamma * Q2[next_state][max_next_action] - Q1[state][action])

    def get_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        else:
            if state not in self.Q1:
                self.Q1[state] = {a: 0.0 for a in self.actions}
                self.Q2[state] = {a: 0.0 for a in self.actions}
            max_action = max(self.Q1[state], key=self.Q1[state].get)
            return max_action

