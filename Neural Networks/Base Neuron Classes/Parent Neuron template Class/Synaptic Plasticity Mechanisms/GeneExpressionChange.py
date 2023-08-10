import numpy as np

class GeneExpressionChange:
    def __init__(self, gene_activity_threshold, learning_rate, noise_std_dev):
        self.gene_activity_threshold = gene_activity_threshold
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_gene_expression(self, gene_expression, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        if activity_level >= self.gene_activity_threshold:
            gene_expression += self.learning_rate * activity_level
        else:
            gene_expression -= self.learning_rate * activity_level

        return gene_expression

