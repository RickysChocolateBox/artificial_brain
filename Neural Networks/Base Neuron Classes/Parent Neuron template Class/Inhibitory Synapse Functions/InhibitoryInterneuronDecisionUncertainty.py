import numpy as np

class InhibitoryInterneuronDecisionUncertainty:
    def __init__(self, num_neurons, inhibition_strength=0.5, time_scale=5):
        self.num_neurons = num_neurons
        self.inhibition_strength = inhibition_strength
        self.time_scale = time_scale
        self.connectivity_matrix = np.random.uniform(0, inhibition_strength, (num_neurons, num_neurons))
        np.fill_diagonal(self.connectivity_matrix, 0)

    def compute_inhibition(self, pre_activity, post_activity):
        inhibition = np.dot(pre_activity, self.connectivity_matrix * post_activity[:, None])
        return inhibition

    def update_connectivity(self, pre_activity, post_activity):
        delta_conn = np.outer(pre_activity, post_activity) * self.inhibition_strength
        self.connectivity_matrix -= delta_conn / self.time_scale
        np.fill_diagonal(self.connectivity_matrix, 0)
        self.connectivity_matrix.clip(min=0, max=self.inhibition_strength, out=self.connectivity_matrix)

    def update_activity(self, current_activity, decision_uncertainty, dt):
        uncertain_neurons = decision_uncertainty >= 0.5
        inhibition = self.compute_inhibition(current_activity, uncertain_neurons)
        new_activity = current_activity - inhibition * dt
        new_activity.clip(min=0, max=1, out=new_activity)
        return new_activity

    def adjust_inhibition_strength(self, decision_uncertainty):
        self.inhibition_strength = 0.5 + 0.5 * decision_uncertainty

    def integrate_decision_uncertainty(self, activity_levels, decision_uncertainty, dt):
        self.adjust_inhibition_strength(np.mean(decision_uncertainty))
        next_activity_levels = self.update_activity(activity_levels, decision_uncertainty, dt)
        self.update_connectivity(activity_levels, next_activity_levels)
        return next_activity_levels

