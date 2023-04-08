class IntrinsicMotivationQAgent:
    def __init__(self, state_size, action_size, learning_rate, discount_factor, exploration_rate):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        self.q_table = np.zeros((state_size, action_size))
        self.intrinsic_rewards = np.zeros((state_size, action_size))

    def update(self, state, action, reward, next_state, done):
        intrinsic_reward = self.compute_intrinsic_reward(state, action)
        total_reward = reward + intrinsic_reward

        target = total_reward + self.discount_factor * np.max(self.q_table[next_state])
        self.q_table[state, action] += self.learning_rate * (target - self.q_table[state, action])

        if done:
            self.exploration_rate *= 0.99

    def compute_intrinsic_reward(self, state, action):
        self.intrinsic_rewards[state, action] += 1
        return 1 / np.sqrt(self.intrinsic_rewards[state, action])

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.action_size)
        else:
            return np.argmax(self.q_table[state])

