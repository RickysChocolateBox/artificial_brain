import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.distributions import Categorical

class PPO:
    def __init__(self, state_dim, action_dim, lr, gamma, clip_param):
        self.policy = Policy(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)
        self.gamma = gamma
        self.clip_param = clip_param

    def select_action(self, state):
        state = torch.from_numpy(state).float().unsqueeze(0)
        probs = self.policy(state)
        dist = Categorical(probs)
        action = dist.sample()
        return action.item(), dist.log_prob(action)

    def update(self, rollouts):
        states = rollouts.states
        actions = rollouts.actions
        rewards = rollouts.rewards
        masks = rollouts.masks
        old_log_probs = rollouts.log_probs

        returns = compute_returns(rewards, masks, self.gamma)

        advantages = compute_advantages(returns, states, self.policy, self.gamma)

        for _ in range(10):
            sampler = BatchSampler(SubsetRandomSampler(range(states.size(0))), batch_size=64, drop_last=False)
            for indices in sampler:
                batch_states = states[indices]
                batch_actions = actions[indices]
                batch_old_log_probs = old_log_probs[indices]
                batch_returns = returns[indices]
                batch_advantages = advantages[indices]

                new_log_probs = self.policy.evaluate(batch_states, batch_actions)
                ratio = torch.exp(new_log_probs - batch_old_log_probs)

                surr1 = ratio * batch_advantages
                surr2 = torch.clamp(ratio, 1.0 - self.clip_param, 1.0 + self.clip_param) * batch_advantages

                policy_loss = -torch.min(surr1, surr2).mean()
                value_loss = F.mse_loss(self.policy.get_value(batch_states).squeeze(), batch_returns)

                self.optimizer.zero_grad()
                (policy_loss + value_loss).backward()
                self.optimizer.step()

def compute_returns(rewards, masks, gamma):
    returns = torch.zeros_like(rewards)
    running_returns = 0
    for t in reversed(range(0, rewards.size(0))):
        running_returns = rewards[t] + gamma * running_returns * masks[t]
        returns[t] = running_returns
    return returns

def compute_advantages(returns, states, policy, gamma, tau=0.95):
    advantages = torch.zeros_like(returns)
    values = policy.get_value(states).detach()
    running_advantage = 0
    for t in reversed(range(0, returns.size(0))):
        delta = returns[t] - values[t]
        running_advantage = delta + gamma * tau * running_advantage
        advantages[t] = running_advantage
    return advantages
        

class Policy(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(Policy, self).__init__()
        self.fc1 = nn.Linear(state_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        self.actor = nn.Linear(64, action_dim)
        self.critic = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return F.softmax(self.actor(x), dim=1)

    def evaluate(self, state, action):
        probs = self.forward(state)
        dist = Categorical(probs)
       

