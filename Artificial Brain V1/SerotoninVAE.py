import numpy as np
import tensorflow as tf
class SerotoninVAE:
    def __init__(self, alpha):
        self.alpha = alpha
        
    def update_alpha(self, epoch):
        if epoch < 10:
            self.alpha = 0.1
        elif epoch < 50:
            self.alpha = 0.01
        else:
            self.alpha = 0.001
        
    def update_output(self, output):
        return tf.nn.sigmoid(self.alpha * output)
