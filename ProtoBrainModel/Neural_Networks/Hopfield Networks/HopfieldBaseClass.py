import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons, neurotransmitter_classes=None):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))
        self.neurotransmitter_classes = neurotransmitter_classes if neurotransmitter_classes is not None else []

    def train(self, patterns):
        patterns = [self._convert_pattern(pattern) for pattern in patterns]

        for p in patterns:
            self.weights += np.outer(p, p)
        np.fill_diagonal(self.weights, 0)

    def predict(self, input_pattern, num_iterations=100):
        input_pattern = self._convert_pattern(input_pattern)
        output_pattern = np.copy(input_pattern)

        for _ in range(num_iterations):
            for i in range(self.num_neurons):
                output_pattern[i] = 1 if np.dot(self.weights[i], output_pattern) >= 0 else -1

        return self._convert_pattern(output_pattern, back_to_original=True)

    def update_neurotransmitter_levels(self, toolkit_report):
        for neurotransmitter_class in self.neurotransmitter_classes:
            neurotransmitter = neurotransmitter_class()

            if hasattr(neurotransmitter, 'learning_rate'):
                self.learning_rate = neurotransmitter.learning_rate

    def _convert_pattern(self, pattern, back_to_original=False):
        if back_to_original:
            return [1 if elem == 1 else 0 for elem in pattern]
        else:
            return [1 if elem == 1 else -1 for elem in pattern]
