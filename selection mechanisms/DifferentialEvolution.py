import numpy as np

class DifferentialEvolution:
    def __init__(self, population_size, mutation_factor, crossover_probability):
        self.population_size = population_size
        self.mutation_factor = mutation_factor
        self.crossover_probability = crossover_probability

    def optimize(self, fitness_func, bounds, max_iterations):
        dimensions = len(bounds)
        population = np.random.rand(self.population_size, dimensions)
        min_bounds, max_bounds = np.asarray(bounds).T
        diff = max_bounds - min_bounds
        initial_population = min_bounds + population * diff
        fitness_values = np.asarray([fitness_func(ind) for ind in initial_population])
        best_index = np.argmin(fitness_values)
        best_individual = initial_population[best_index]

        for i in range(max_iterations):
            for j in range(self.population_size):
                indices = [index for index in range(self.population_size) if index != j]
                x0, x1, x2 = population[np.random.choice(indices, 3, replace=False)]
                mutant_individual = x0 + self.mutation_factor * (x1 - x2)
                mutant_individual = np.clip(mutant_individual, 0, 1)

                crossover = np.random.rand(dimensions) < self.crossover_probability
                if not np.any(crossover):
                    crossover[np.random.randint(0, dimensions)] = True

                trial_individual = np.where(crossover, mutant_individual, population[j])
                trial_individual = np.clip(trial_individual, 0, 1)

                f = fitness_func(trial_individual)
                if f < fitness_values[j]:
                    fitness_values[j] = f
                    population[j] = trial_individual

                    if f < fitness_values[best_index]:
                        best_index = j
                        best_individual = trial_individual

        return best_individual, fitness_func(best_individual)

