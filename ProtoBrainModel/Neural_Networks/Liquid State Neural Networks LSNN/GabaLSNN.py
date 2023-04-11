import torch
import torch.nn.functional as F

class GabaLSNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size, tau, dt):
        super(GabaLSNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.tau = tau
        self.dt = dt
        self.W_in = torch.randn(hidden_size, input_size) / torch.sqrt(torch.tensor(input_size).float())
        self.W_rec = torch.randn(hidden_size, hidden_size) / torch.sqrt(torch.tensor(hidden_size).float())
        self.W_out = torch.randn(output_size, hidden_size) / torch.sqrt(torch.tensor(hidden_size).float())
        self.I_bias = torch.zeros(hidden_size)
        self.G_bias = torch.zeros(hidden_size)
        self.reset_states()

    def reset_states(self):
        self.h = torch.zeros(self.hidden_size)
        self.r = torch.zeros(self.hidden_size)
        self.z = torch.zeros(self.hidden_size)

    def forward(self, x):
        T = x.shape[0]
        y = torch.zeros(T, self.output_size)
        for t in range(T):
            i_t = torch.matmul(self.W_in, x[t])
            r_t = torch.matmul(self.W_rec, self.h)
            g_t = torch.sigmoid(self.G_bias + r_t)
            z_t = torch.tanh(i_t + g_t * r_t)
            self.h += (1.0 / self.tau) * (z_t - self.h) * self.dt
            y[t] = torch.matmul(self.W_out, self.h)
        return y

    def gaba_release(self):
        self.W_rec = F.dropout(self.W_rec, p=0.2)


