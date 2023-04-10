import numpy as np

class BatchNormalization:
    def __init__(self, momentum=0.99, epsilon=1e-3):
        self.momentum = momentum
        self.epsilon = epsilon
        self.running_mean = None
        self.running_var = None
        self.gamma = None
        self.beta = None
        self.train_mode = True

    def forward(self, x):
        if self.running_mean is None:
            N, D = x.shape
            self.running_mean = np.zeros(D)
            self.running_var = np.zeros(D)

        if self.train_mode:
            batch_mean = np.mean(x, axis=0)
            batch_var = np.var(x, axis=0)
            self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * batch_mean
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * batch_var

            x_norm = (x - batch_mean) / np.sqrt(batch_var + self.epsilon)
            out = self.gamma * x_norm + self.beta

        else:
            x_norm = (x - self.running_mean) / np.sqrt(self.running_var + self.epsilon)
            out = self.gamma * x_norm + self.beta

        return out

    def backward(self, dout):
        N = dout.shape[0]
        x_norm = self.x_norm
        x_mu = self.x - self.mean
        std_inv = 1.0 / self.std
        dgamma = np.sum(dout * x_norm, axis=0)
        dbeta = np.sum(dout, axis=0)

        dx_norm = dout * self.gamma
        dx = (1.0 / N) * std_inv * (N*dx_norm - np.sum(dx_norm, axis=0) - x_norm*np.sum(dx_norm*x_norm, axis=0))
        dgamma /= N
        dbeta /= N

        self.gamma += -self.learning_rate * dgamma
        self.beta += -self.learning_rate * dbeta

        return dx

