import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class AdversarialTraining:
    def __init__(self, model, criterion, optimizer, epsilon=0.05, alpha=0.1):
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
        self.epsilon = epsilon
        self.alpha = alpha

    def train(self, train_loader, num_epochs):
        self.model.train()
        for epoch in range(num_epochs):
            for i, (images, labels) in enumerate(train_loader):
                images = images.cuda()
                labels = labels.cuda()

                # Adversarial perturbation
                perturbation = self.create_perturbation(images)
                adversarial_images = self.apply_perturbation(images, perturbation)

                # Forward pass
                outputs = self.model(images)
                loss = self.criterion(outputs, labels)

                # Backward pass
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                # Adversarial training
                adversarial_outputs = self.model(adversarial_images)
                adversarial_loss = self.criterion(adversarial_outputs, labels)
                adversarial_loss.backward()
                self.optimizer.step()

    def create_perturbation(self, images):
        perturbation = torch.zeros_like(images)
        perturbation = perturbation.uniform_(-self.epsilon, self.epsilon)
        perturbation = perturbation.to(images.device)
        return perturbation

    def apply_perturbation(self, images, perturbation):
        adversarial_images = images.clone().detach() + perturbation
        adversarial_images = torch.clamp(adversarial_images, 0, 1)
        return adversarial_images

