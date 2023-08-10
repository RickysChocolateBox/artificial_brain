import numpy as np

class MTORSignalingRegulation:
    def __init__(self, mtor_rate, learning_rate, activation_function, threshold):
        self.mtor_rate = mtor_rate
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        self.threshold = threshold

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def apply_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return self.sigmoid(x)
        elif self.activation_function == 'relu':
            return self.relu(x)

    def update_mtor_signaling(self, mtor_activity, activity_level):
        activity_level = self.apply_activation_function(activity_level)
        change_in_mtor_activity = self.mtor_rate * activity_level
        mtor_activity += self.learning_rate * change_in_mtor_activity
        mtor_activity = np.clip(mtor_activity, -self.threshold, self.threshold)
        return mtor_activity

