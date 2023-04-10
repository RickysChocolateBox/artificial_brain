import random

class NeurotransmitterTuner:

    def __init__(self, neural_network_instances, main_ann_callback, toolkit):
        self.neural_network_instances = neural_network_instances
        self.main_ann_callback = main_ann_callback
        self.toolkit = toolkit

    def optimize_neurotransmitter_levels(self, y_true, y_pred):
        proposed_neurotransmitter_levels = self.propose_neurotransmitter_levels()
        approved_neurotransmitter_levels = self.main_ann_callback(proposed_neurotransmitter_levels)
        self.apply_neurotransmitter_levels(approved_neurotransmitter_levels)
        self.evaluate_and_report_fitness(y_true, y_pred)

    def propose_neurotransmitter_levels(self):
        proposed_levels = {}
        for nn in self.neural_network_instances:
            proposed_levels[nn] = random.uniform(0.1, 1.0)
        return proposed_levels

    def apply_neurotransmitter_levels(self, neurotransmitter_levels):
        for nn, level in neurotransmitter_levels.items():
            nn.set_neurotransmitter_level(level)

    def evaluate_and_report_fitness(self, y_true, y_pred):
        function_name, selected_gradient_objective_function = self.toolkit.ucb1_select_gradient_objective_function()
        performance = selected_gradient_objective_function(y_true, y_pred)
        self.toolkit.report_action({"function_name": function_name, "performance": performance})

