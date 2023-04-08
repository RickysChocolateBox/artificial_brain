import numpy as np

class SARSA:
    def __init__(self, state_size, action_size, learning_rate, discount_factor, exploration_rate):
        self.Q = np.zeros((state_size, action_size)) # Initialize Q values to 0
        self.learning_rate = learning_rate # Learning rate
        self.discount_factor = discount_factor # Discount factor
        self.exploration_rate = exploration_rate # Exploration rate
        self.action_size = action_size # Number of possible actions
        self.state_size = state_size # Size of the state space
        self.prev_state = None # Keep track of the previous state
        self.prev_action = None # Keep track of the previous action

    def select_action(self, state):
        # Select the next action based on the exploration rate and the current state
        if np.random.uniform() < self.exploration_rate:
            return np.random.choice(self.action_size)
        else:
            return np.argmax(self.Q[state, :])

    def update(self, state, reward, done):
        if done:
            # If the episode is done, update the Q value using the terminal state and reward
            td_target = reward
            td_error = td_target - self.Q[self.prev_state, self.prev_action]
            self.Q[self.prev_state, self.prev_action] += self.learning_rate * td_error
            return

        # Select the next action based on the exploration rate and the current state
        action = self.select_action(state)

        if self.prev_state is not None and self.prev_action is not None:
            # Update the Q value using the previous state, action, and the current state, reward, and action
            td_target = reward + self.discount_factor * self.Q[state, action]
            td_error = td_target - self.Q[self.prev_state, self.prev_action]
            self.Q[self.prev_state, self.prev_action] += self.learning_rate * td_error

        self.prev_state = state # Update the previous state
        self.prev_action = action # Update the previous action

