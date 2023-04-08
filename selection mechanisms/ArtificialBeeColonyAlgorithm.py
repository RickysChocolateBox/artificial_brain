import numpy as np

class ArtificialBeeColonyAlgorithm:
    def __init__(self, objective_function, num_employed_bees, num_onlooker_bees, num_cycles, lower_bounds, upper_bounds):
        self.objective_function = objective_function
        self.num_employed_bees = num_employed_bees
        self.num_onlooker_bees = num_onlooker_bees
        self.num_cycles = num_cycles
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

        self.best_solution = None
        self.best_fitness = np.inf
        self.current_solution = None
        self.current_fitness = None

        self.initialize_solutions()

    def initialize_solutions(self):
        self.solutions = np.random.uniform(self.lower_bounds, self.upper_bounds, size=(self.num_employed_bees, len(self.lower_bounds)))
        self.fitness_values = np.array([self.objective_function(solution) for solution in self.solutions])
        self.onlooker_probabilities = self.fitness_values / np.sum(self.fitness_values)

    def optimize(self):
        for cycle in range(self.num_cycles):
            # Employed bees phase
            for i in range(self.num_employed_bees):
                candidate_solution = self.solutions[i].copy()
                j = np.random.choice([j for j in range(self.num_employed_bees) if j != i])
                k = np.random.randint(0, len(self.lower_bounds))
                candidate_solution[k] = self.solutions[i][k] + np.random.uniform(low=-1, high=1) * (self.solutions[i][k] - self.solutions[j][k])

                candidate_fitness = self.objective_function(candidate_solution)
                if candidate_fitness < self.fitness_values[i]:
                    self.solutions[i] = candidate_solution
                    self.fitness_values[i] = candidate_fitness

            # Onlooker bees phase
            for i in range(self.num_onlooker_bees):
                i = np.random.choice([i for i in range(self.num_employed_bees)], p=self.onlooker_probabilities)
                candidate_solution = self.solutions[i].copy()
                j = np.random.choice([j for j in range(self.num_employed_bees) if j != i])
                k = np.random.randint(0, len(self.lower_bounds))
                candidate_solution[k] = self.solutions[i][k] + np.random.uniform(low=-1, high=1) * (self.solutions[i][k] - self.solutions[j][k])

                candidate_fitness = self.objective_function(candidate_solution)
                if candidate_fitness < self.fitness_values[i]:
                    self.solutions[i] = candidate_solution
                    self.fitness_values[i] = candidate_fitness

            # Memorize the best solution
            self.current_solution = self.solutions[np.argmin(self.fitness_values)]
            self.current_fitness = np.min(self.fitness_values)
            if self.current_fitness < self.best_fitness:
                self.best_solution = self.current_solution
                self.best_fitness = self.current_fitness

            # Update onlooker probabilities
            self.onlooker_probabilities = self.fitness_values / np.sum(self.fitness_values)

        return self.best_solution, self.best_fitness

