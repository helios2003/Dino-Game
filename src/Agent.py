import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import PolicyNetwork

class Agent:
    def __init__(self, input_size, output_size):
        """
        The following parameters are initialized:
        input_size: The number of input neurons
        output_size: The number of output neurons
        gamma: The discount factor
        eps: A small value used to avoid division by zero
        lr: The learning rate
        optimizer: The optimizer used to update the weights of the policy network
        """
        self.policy_net = PolicyNetwork(input_size, output_size)
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=0.01)
        self.gamma = 0.95
        self.eps = np.finfo(np.float32).eps.item()

    def select_action(self, state):
        """
        The actions are selected based on the policy network's output probabilities
        """
        state = torch.from_numpy(state).type(torch.FloatTensor)
        action_probs = self.policy_net(state)
        action = np.random.choice(np.arange(len(action_probs)), p=action_probs.detach().numpy())
        return action
    
    def update_policy(self, rewards, log_probs):
        """
        The policy network is updated using the Policy Gradient algorithm
        The algorithm is as follows:
        1. Calculate the discounted rewards
        2. Calculate the policy gradient
        3. Update the weights of the policy network
        4. Reset the gradients to zero
        """
        discounted_rewards = []
        for t in range(len(rewards)):
            Gt = 0
            pw = 0
            for r in rewards[t:]:
                Gt = Gt + self.gamma ** pw * r   # Discounted reward
                pw = pw + 1 
            discounted_rewards.append(Gt)
        discounted_rewards = torch.tensor(discounted_rewards)
        discounted_rewards = (discounted_rewards - discounted_rewards.mean()) / (discounted_rewards.std() + self.eps)
        policy_gradient = []
        for log_prob, Gt in zip(log_probs, discounted_rewards):
            policy_gradient.append(-log_prob * Gt)
        self.optimizer.zero_grad()
        # Sum the gradients of the policy network
        policy_gradient = torch.stack(policy_gradient).sum()
        # Backpropagation
        policy_gradient.backward()
        self.optimizer.step()