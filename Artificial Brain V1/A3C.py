import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import gym
import numpy as np
import math
import time
import threading
from collections import deque
from torch.distributions import Categorical

class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.actor = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
            nn.Softmax(dim=-1)
        )
        self.critic = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, state):
        action_probs = self.actor(state)
        value = self.critic(state)
        return action_probs, value

class A3C:
    def __init__(self, env, gamma=0.99, lr=0.001, num_processes=4, max_steps=1000, num_episodes=1000):
        self.env = env
        self.gamma = gamma
        self.lr = lr
        self.num_processes = num_processes
        self.max_steps = max_steps
        self.num_episodes = num_episodes
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        
        self.model = ActorCritic(env.observation_space.shape[0], env.action_space.n).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr)
        
        self.processes = []
        self.episode_rewards = deque(maxlen=100)
        self.scores = []
        self.scores_lock = threading.Lock()
        self.entropy_weight = 0.01
        
    def train(self):
        for i in range(self.num_processes):
            self.processes.append(threading.Thread(target=self.run, args=(i,)))
            
        for process in self.processes:
            process.start()
            
        for process in self.processes:
            process.join()
        
    def run(self, process_id):
        env = gym.make(self.env)
        state = env.reset()
        done = False
        episode_reward = 0
        steps = 0
        
        while steps < self.max_steps:
            log_probs, value = self.model(torch.FloatTensor(state).to(self.device))
            probs = F.softmax(log_probs, dim=0)
            action = Categorical(probs).sample().cpu().numpy()
            
            next_state, reward, done, _ = env.step(action)
            episode_reward += reward
            steps += 1
            
            if done or steps == self.max_steps:
                with self.scores_lock:
                    self.episode_rewards.append(episode_reward)
                    
                self.scores.append(episode_reward)
                state = env.reset()
                done = False
                episode_reward = 0
                steps = 0
            else:
                state = next_state
            
            if len(self.episode_rewards) == self.episode_rewards.maxlen:
                avg_reward = np.mean(self.episode_rewards)
                if avg_reward >= self.env.spec.reward_threshold:
                    print(f"Solved environment in {len(self.scores)} episodes.")
                    break
            
            if steps % self.num_processes == 0:
                self.update_model()
                
    def update_model(self):
        states = []
        actions = []
        rewards = []
        log_probs = []
        values = []
        
        for i in range(self.num_processes):
            states.append([])
            actions.append([])
            rewards.append([])
            log_probs.append([])
            values.append([])
            
        envs = [gym.make(self.env) for i in range(self.num_processes)]
        states = [env.reset() for env in envs]
        done = [False for i in range(self.num_processes)]
        steps = [0 for i in range(self.num_processes)]
        
        while not all(done):
            for i in range(self.num_processes):
                log_prob, value = self.model(torch.FloatTensor(states[i]).to(self.device))
                probs = F.softmax(log_prob, dim=0)
                action = Categorical(probs).sample().cpu().numpy

                
                actions[i].append(int(action))
                log_probs[i].append(log_prob)
                values[i].append(value)
                
                
