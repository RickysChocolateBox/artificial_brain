import numpy as np

class FireflyAlgorithm:
    def __init__(self, objective_function, num_variables, lower_bound, upper_bound, alpha, beta_min, gamma):
        self.objective_function = objective_function
        self.num_variables = num_variables
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.alpha = alpha
        self.beta_min = beta_min
        self.gamma = gamma

    def optimize(self, num_iterations, num_fireflies):
        # Initialize fireflies with random positions
        positions = np.random.uniform(self.lower_bound, self.upper_bound, (num_fireflies, self.num_variables))
        intensities = np.array([self.objective_function(x) for x in positions])
        
        for i in range(num_iterations):
            # Update the brightness of each firefly
            for j in range(num_fireflies):
                for k in range(num_fireflies):
                    if intensities[j] < intensities[k]:
                        r = np.sqrt(np.sum((positions[j] - positions[k]) ** 2))
                        beta = self.beta_min * np.exp(-self.gamma * r ** 2)
                        positions[j] += self.alpha * beta * (positions[k] - positions[j]) + np.random.normal(size=self.num_variables)
                        positions[j] = np.clip(positions[j], self.lower_bound, self.upper_bound)
                        intensities[j] = self.objective_function(positions[j])
        
        # Return the best solution found
        best_index = np.argmin(intensities)
        return positions[best_index], intensities[best_index]

