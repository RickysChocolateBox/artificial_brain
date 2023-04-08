import random

class GeneticAlgorithm:
    def __init__(self, fitness_func, chromosome_length, pop_size=100, mutation_rate=0.01, crossover_rate=0.9, elitism=True):
        self.fitness_func = fitness_func
        self.chromosome_length = chromosome_length
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism

        self.population = []
        for i in range(pop_size):
            self.population.append([random.randint(0, 1) for _ in range(chromosome_length)])
        
    def evolve(self, generations=100):
        for i in range(generations):
            self.evaluate()
            new_pop = []
            while len(new_pop) < self.pop_size:
                parent1 = self.selection()
                parent2 = self.selection()
                offspring1, offspring2 = self.crossover(parent1, parent2)
                offspring1 = self.mutate(offspring1)
                offspring2 = self.mutate(offspring2)
                new_pop.append(offspring1)
                if len(new_pop) < self.pop_size:
                    new_pop.append(offspring2)
            self.population = new_pop

    def evaluate(self):
        fitnesses = [self.fitness_func(chromosome) for chromosome in self.population]
        self.fitnesses = fitnesses

    def selection(self):
        total_fitness = sum(self.fitnesses)
        r = random.uniform(0, total_fitness)
        running_total = 0
        for i in range(len(self.population)):
            running_total += self.fitnesses[i]
            if running_total > r:
                return self.population[i]

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.chromosome_length - 1)
            offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
            offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        else:
            offspring1 = parent1
            offspring2 = parent2
        return offspring1, offspring2

    def mutate(self, offspring):
        for i in range(len(offspring)):
            if random.random() < self.mutation_rate:
                offspring[i] = 1 - offspring[i]
        return offspring

