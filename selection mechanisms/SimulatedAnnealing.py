import random
import math

class SimulatedAnnealing:
    def __init__(self, initial_temperature, cooling_factor):
        self.initial_temperature = initial_temperature
        self.cooling_factor = cooling_factor
        
    def optimize(self, cost_function, initial_solution):
        current_solution = initial_solution
        current_cost = cost_function(current_solution)
        temperature = self.initial_temperature
        
        while temperature > 1e-6:
            # Generate a new candidate solution by making a small random change
            candidate_solution = current_solution + random.gauss(0, temperature)
            candidate_cost = cost_function(candidate_solution)
            
            # Determine if we should accept the candidate solution
            delta_cost = candidate_cost - current_cost
            if delta_cost < 0 or math.exp(-delta_cost / temperature) > random.random():
                current_solution = candidate_solution
                current_cost = candidate_cost
            
            # Decrease the temperature
            temperature *= self.cooling_factor
        
        return current_solution, current_cost

