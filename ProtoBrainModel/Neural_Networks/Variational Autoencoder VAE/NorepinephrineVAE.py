import numpy as np
import tensorflow as tf
class NorepinephrineVAE:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        
    def adjust_learning_rate(self, epoch):
        if epoch < 10:
            self.learning_rate = 0.001
        elif epoch < 50:
            self.learning_rate = 0.0001
        else:
            self.learning_rate = 0.00001
        
    def optimizer(self, loss):
        optimizer = tf.keras.optimizers.Adam(lr=self.learning_rate)
        return optimizer.minimize(loss)
