import numpy as np

class MonteCarlo:
    def __init__(self, env, gamma=0.99, alpha=0.1, epsilon=1.0, epsilon_decay=0.9999, epsilon_min=0.01):
        self.env = env
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = {}
        self.n_table = {}

    def get_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0] * self.env.action_space.n
            self.n_table[state] = [0] * self.env.action_space.n

        if np.random.uniform() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])

    def update(self, state, action, reward, trajectory):
        for t, (s, a, r) in enumerate(trajectory):
            if s not in self.q_table:
                self.q_table[s] = [0] * self.env.action_space.n
                self.n_table[s] = [0] * self.env.action_space.n

            self.n_table[s][a] += 1
            alpha = 1 / self.n_table[s][a]
            G = sum([self.gamma**i * r for i, (_, _, r) in enumerate(trajectory[t:])])
            self.q_table[s][a] += alpha * (G - self.q_table[s][a])

        self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)

