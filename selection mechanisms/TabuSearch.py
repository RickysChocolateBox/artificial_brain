class TabuSearch:
    def __init__(self, max_iterations, tabu_list_size):
        self.max_iterations = max_iterations
        self.tabu_list_size = tabu_list_size

    def search(self, initial_solution, neighborhood_function, objective_function):
        current_solution = initial_solution
        best_solution = current_solution
        tabu_list = []

        for i in range(self.max_iterations):
            neighborhood = neighborhood_function(current_solution)
            best_neighbor = None
            best_neighbor_value = float('inf')

            for neighbor in neighborhood:
                if neighbor not in tabu_list:
                    neighbor_value = objective_function(neighbor)
                    if neighbor_value < best_neighbor_value:
                        best_neighbor = neighbor
                        best_neighbor_value = neighbor_value

            if best_neighbor is None:
                break

            current_solution = best_neighbor

            if best_neighbor_value < objective_function(best_solution):
                best_solution = best_neighbor

            tabu_list.append(best_neighbor)
            if len(tabu_list) > self.tabu_list_size:
                tabu_list.pop(0)

        return best_solution

