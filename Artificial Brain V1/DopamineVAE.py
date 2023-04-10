import numpy as np
import tensorflow as tf
class DopamineVAE:
    def __init__(self, beta):
        self.beta = beta
        
    def update_beta(self, epoch):
        if epoch < 10:
            self.beta = 0.001
        elif epoch < 50:
            self.beta = 0.01
        else:
            self.beta = 0.1
        
    def update_loss(self, loss, z_mean, z_log_var):
        kl_loss = -0.5 * tf.reduce_mean(1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var))
        return loss + self.beta * kl_loss
