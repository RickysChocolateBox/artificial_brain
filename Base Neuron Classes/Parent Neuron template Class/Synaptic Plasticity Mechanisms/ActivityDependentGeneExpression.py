import numpy as np

class ActivityDependentGeneExpression:
    def __init__(self, expression_rate, modulation_threshold, noise_std_dev):
        self.expression_rate = expression_rate
        self.modulation_threshold = modulation_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update gene expression based on activity level and random noise
    def update_expression(self, gene_expression, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Adjust gene expression based on activity level
        if activity_level >= self.modulation_threshold:
            gene_expression *= (1 + self.expression_rate)
        else:
            gene_expression *= (1 - self.expression_rate)

        return gene_expression

# This class represents the mechanism of activity-dependent gene expression. The primary function, update_expression, adjusts gene expression based on the activity level and random noise. If the activity level is above the modulation_threshold, gene expression is increased. Otherwise, it is decreased. The sigmoid function is used as the activation function.