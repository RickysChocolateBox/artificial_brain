import random

class HarmonySearchAlgorithm:
    def __init__(self, problem_size, objective_function, max_iterations=100, harmony_memory_size=20, pitch_adjustment_rate=0.05):
        self.problem_size = problem_size
        self.objective_function = objective_function
        self.max_iterations = max_iterations
        self.harmony_memory_size = harmony_memory_size
        self.pitch_adjustment_rate = pitch_adjustment_rate
        self.harmony_memory = self.initialize_harmony_memory()

    def initialize_harmony_memory(self):
        harmony_memory = []
        for i in range(self.harmony_memory_size):
            harmony = [random.uniform(0, 1) for j in range(self.problem_size)]
            harmony_memory.append(harmony)
        return harmony_memory

    def get_new_harmony(self):
        harmony = [random.uniform(0, 1) for i in range(self.problem_size)]
        return harmony

    def adjust_pitch(self, harmony):
        for i in range(len(harmony)):
            if random.uniform(0, 1) < self.pitch_adjustment_rate:
                harmony[i] += random.uniform(-0.1, 0.1)
                harmony[i] = max(min(harmony[i], 1), 0)
        return harmony

    def run(self):
        best_solution = None
        best_fitness = float('inf')

        for iteration in range(self.max_iterations):
            new_harmony = self.get_new_harmony()
            new_harmony = self.adjust_pitch(new_harmony)

            worst_index = -1
            worst_fitness = float('-inf')
            for i in range(len(self.harmony_memory)):
                fitness = self.objective_function(self.harmony_memory[i])
                if fitness > worst_fitness:
                    worst_fitness = fitness
                    worst_index = i

            if self.objective_function(new_harmony) < worst_fitness:
                self.harmony_memory[worst_index] = new_harmony

            for harmony in self.harmony_memory:
                fitness = self.objective_function(harmony)
                if fitness < best_fitness:
                    best_fitness = fitness
                    best_solution = harmony

        return best_solution, best_fitness

