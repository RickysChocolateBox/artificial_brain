import numpy as np

class InhibitoryInterneuronPlanning:
    def __init__(self, num_neurons, inhibition_strength=0.5, planning_threshold=0.8, learning_rate=0.01, plan_memory_size=5):
        self.num_neurons = num_neurons
        self.inhibition_strength = inhibition_strength
        self.planning_threshold = planning_threshold
        self.learning_rate = learning_rate
        self.plan_memory_size = plan_memory_size
        self.connectivity_matrix = np.random.uniform(0, inhibition_strength, (num_neurons, num_neurons))
        np.fill_diagonal(self.connectivity_matrix, 0)
        self.memory_matrix = np.zeros((num_neurons, plan_memory_size))

    def compute_inhibition(self, pre_activity, post_activity):
        inhibition = np.dot(pre_activity, self.connectivity_matrix * post_activity[:, None])
        return inhibition

    def update_weights(self, activity_levels):
        self.connectivity_matrix += self.learning_rate * np.outer(activity_levels, activity_levels)
        np.fill_diagonal(self.connectivity_matrix, 0)
        self.connectivity_matrix.clip(min=0, max=self.inhibition_strength, out=self.connectivity_matrix)

    def update_memory(self, activity_levels):
        self.memory_matrix[:, :-1] = self.memory_matrix[:, 1:]
        self.memory_matrix[:, -1] = activity_levels

    def update_activity(self, activity_levels):
        high_activity_neurons = activity_levels >= self.planning_threshold
        inhibition = self.compute_inhibition(activity_levels, high_activity_neurons)
        activity_levels -= inhibition
        activity_levels.clip(min=0, max=1, out=activity_levels)
        self.update_weights(activity_levels)
        self.update_memory(activity_levels)
        return activity_levels

    def get_plans(self):
        plan_indices = np.argsort(self.memory_matrix, axis=1)[:, -self.plan_memory_size:]
        return plan_indices

