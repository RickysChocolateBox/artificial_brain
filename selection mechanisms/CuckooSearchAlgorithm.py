import numpy as np

class CuckooSearchAlgorithm:
    def __init__(self, fitness_function, num_dimensions, population_size, num_iterations, step_size=0.01, pa=0.25):
        self.fitness_function = fitness_function
        self.num_dimensions = num_dimensions
        self.population_size = population_size
        self.num_iterations = num_iterations
        self.step_size = step_size
        self.pa = pa

    def initialize_population(self):
        population = np.random.uniform(-10, 10, (self.population_size, self.num_dimensions))
        return population

    def levy_flight(self):
        sigma_u = (np.math.gamma(1 + self.step_size) * np.sin(np.pi * self.step_size / 2)) / (np.math.gamma((1 + self.step_size) / 2) * self.step_size * 2 ** ((self.step_size - 1) / 2))
        sigma_v = 1
        u = np.random.normal(0, sigma_u, self.num_dimensions)
        v = np.random.normal(0, sigma_v, self.num_dimensions)
        step = u / np.power(np.fabs(v), 1 / self.step_size)
        return step

    def update_nests(self, population):
        new_population = np.zeros_like(population)
        for i, nest in enumerate(population):
            step = self.levy_flight()
            cuckoo = nest + step
            if np.random.rand() > self.pa:
                random_nest = population[np.random.randint(self.population_size)]
                cuckoo = cuckoo + self.step_size * (cuckoo - random_nest)
            new_population[i] = cuckoo
        return new_population

    def select_best_nests(self, population, new_population):
        merged_population = np.vstack((population, new_population))
        fitness_values = np.apply_along_axis(self.fitness_function, 1, merged_population)
        sorted_indices = np.argsort(fitness_values)
        return merged_population[sorted_indices[:self.population_size]]

    def run(self):
        population = self.initialize_population()
        for i in range(self.num_iterations):
            new_population = self.update_nests(population)
            population = self.select_best_nests(population, new_population)
        return population[0]

