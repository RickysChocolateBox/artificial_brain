import numpy as np
from typing import List, Tuple

class AntColonyOptimization:
    def __init__(self, num_ants: int, num_iterations: int, pheromone_evaporation: float, pheromone_deposit: float, alpha: float, beta: float, q: float):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.pheromone_evaporation = pheromone_evaporation
        self.pheromone_deposit = pheromone_deposit
        self.alpha = alpha
        self.beta = beta
        self.q = q

    def solve(self, graph: np.ndarray, start_node: int) -> Tuple[float, List[int]]:
        # Initialize pheromone matrix
        pheromone_matrix = np.ones(graph.shape) / (graph.shape[0] - 1)
        np.fill_diagonal(pheromone_matrix, 0)

        # Initialize best tour and its length
        best_tour = None
        best_tour_length = np.inf

        # Loop over iterations
        for i in range(self.num_iterations):
            # Initialize ants
            ants = [Ant(start_node) for _ in range(self.num_ants)]

            # Move ants
            for ant in ants:
                ant.visit(start_node)
                for _ in range(graph.shape[0] - 1):
                    next_node = ant.choose_next_node(graph, pheromone_matrix, self.alpha, self.beta)
                    ant.visit(next_node)

                # Update best tour if necessary
                tour_length = ant.get_tour_length(graph)
                if tour_length < best_tour_length:
                    best_tour = ant.get_tour()
                    best_tour_length = tour_length

            # Update pheromone matrix
            pheromone_matrix *= self.pheromone_evaporation
            for ant in ants:
                tour = ant.get_tour()
                for j in range(len(tour) - 1):
                    current_node, next_node = tour[j], tour[j + 1]
                    pheromone_matrix[current_node, next_node] += self.pheromone_deposit / graph[current_node, next_node]
                    pheromone_matrix[next_node, current_node] += self.pheromone_deposit / graph[next_node, current_node]

        return best_tour_length, best_tour


class Ant:
    def __init__(self, start_node):
        self.tour = [start_node]
        self.visited = {start_node}

    def visit(self, node):
        self.tour.append(node)
        self.visited.add(node)

    def get_tour(self):
        return self.tour

    def get_tour_length(self, graph):
        tour_length = 0
        for i in range(len(self.tour) - 1):
            current_node, next_node = self.tour[i], self.tour[i + 1]
            tour_length += graph[current_node, next_node]
        return tour_length

    def choose_next_node(self, graph, pheromone_matrix, alpha, beta):
        current_node = self.tour[-1]
        unvisited_nodes = list(set(range(graph.shape[0])) - self.visited)

        # Compute probabilities of choosing unvisited nodes
        probabilities = np.zeros(graph.shape[0])
        denominator = 0
        for node in unvisited_nodes:
            denominator += np.power(pheromone_matrix[current_node, node], alpha) * np.power(1 / graph[current_node, node], beta)
       
