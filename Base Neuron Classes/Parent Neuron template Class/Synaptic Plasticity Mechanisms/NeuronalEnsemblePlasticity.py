import numpy as np

class NeuronalEnsemblePlasticity:
    def __init__(self, learning_rate, ensemble_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.ensemble_threshold = ensemble_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update the ensemble activation based on activity level and noise
    def update_ensemble_activation(self, ensemble_activation, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update ensemble activation based on activity level
        if activity_level >= self.ensemble_threshold:
            ensemble_activation += self.learning_rate * (1 - ensemble_activation)
        else:
            ensemble_activation -= self.learning_rate * ensemble_activation

        return ensemble_activation

