import numpy as np

class MitochondrialFunction:
    def __init__(self, change_rate, function_threshold, noise_std_dev):
        self.change_rate = change_rate
        self.function_threshold = function_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update mitochondrial function based on activity level and noise
    def update_mitochondrial_function(self, mitochondrial_function, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update mitochondrial function based on activity level
        if activity_level >= self.function_threshold:
            mitochondrial_function += self.change_rate
        else:
            mitochondrial_function -= self.change_rate

        return mitochondrial_function

