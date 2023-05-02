import networkx as nx
import numpy as np

class NeuralNetworkTopology:
    def __init__(self, add_edge_rate, remove_edge_rate, initial_edges=None):
        self.add_edge_rate = add_edge_rate
        self.remove_edge_rate = remove_edge_rate
        self.network = nx.DiGraph()

        if initial_edges:
            self.network.add_edges_from(initial_edges)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def apply_activation_function(self, x):
        return self.sigmoid(x)

    def update_topology(self, activity_levels):
        edges_to_add = int(self.add_edge_rate * len(activity_levels))
        edges_to_remove = int(self.remove_edge_rate * len(activity_levels))

        # Add new edges
        for _ in range(edges_to_add):
            source, target = np.random.choice(len(activity_levels), 2, replace=False)
            weight = self.apply_activation_function(activity_levels[source]) * self.apply_activation_function(activity_levels[target])
            self.network.add_edge(source, target, weight=weight)

        # Remove edges
        for _ in range(edges_to_remove):
            if self.network.edges:
                edge = np.random.choice(list(self.network.edges), 1)[0]
                self.network.remove_edge(*edge)

        return self.network


