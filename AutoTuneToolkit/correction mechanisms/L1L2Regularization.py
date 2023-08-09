import torch
import torch.nn as nn
import torch.optim as optim

class L1L2Regularization:
    def __init__(self, l1_weight=0.01, l2_weight=0.01):
        self.l1_weight = l1_weight
        self.l2_weight = l2_weight
    
    def apply(self, model, optimizer):
        reg_loss = 0
        for name, param in model.named_parameters():
            if 'weight' in name:
                reg_loss += self.l1_weight * torch.norm(param, 1)
                reg_loss += self.l2_weight * torch.norm(param, 2)
        optimizer.zero_grad()
        reg_loss.backward()
        optimizer.step()

