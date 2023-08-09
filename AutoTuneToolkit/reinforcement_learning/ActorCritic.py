import numpy as np

class ActorCritic:
    def __init__(self, state_size, action_size, alpha, gamma, actor_lr, critic_lr):
        self.state_size = state_size
        self.action_size = action_size
        self.alpha = alpha
        self.gamma = gamma
        self.actor_lr = actor_lr
        self.critic_lr = critic_lr
        self.actor_weights = np.random.rand(state_size, action_size)
        self.critic_weights = np.random.rand(state_size, 1)

    def act(self, state):
        action_probs = self.softmax(self.actor_weights[state])
        action = np.random.choice(self.action_size, p=action_probs)
        return action

    def learn(self, state, action, reward, next_state, done):
        td_error = reward + (1 - int(done)) * self.gamma * self.critic_weights[next_state] - self.critic_weights[state]
        self.critic_weights[state] += self.critic_lr * td_error
        delta = np.zeros((self.state_size, self.action_size))
        delta[state, action] = 1
        actor_gradient = delta - self.softmax(self.actor_weights[state])
        self.actor_weights += self.actor_lr * td_error * actor_gradient

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / np.sum(exp_x)


