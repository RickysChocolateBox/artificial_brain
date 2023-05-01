import numpy as np

class IonotropicReceptorExpression:
    def __init__(self, expression_rate, expression_threshold, noise_std_dev):
        self.expression_rate = expression_rate
        self.expression_threshold = expression_threshold
        self.noise_std_dev = noise_std_dev

    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Update ionotropic receptor expression
    def update_expression(self, expression_state, activity_level):
        # Add random noise to the activity level
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        # Update expression state based on activity level
        if activity_level >= self.expression_threshold:
            expression_state += self.expression_rate
        else:
            expression_state -= self.expression_rate

        return expression_state

# This class represents the mechanism of changes in ionotropic receptor expression. The primary function, update_expression, updates the ionotropic receptor expression state based on the activity level and random noise. The expression state is increased or decreased according to the expression_rate depending on whether the activity level is above or below the expression_threshold.