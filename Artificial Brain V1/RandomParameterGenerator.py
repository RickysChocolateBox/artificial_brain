import random
import math

class RandomParameterGenerator:
    def __init__(self, pattern_ranges, max_weight=5, max_components=3):
        self.pattern_ranges = pattern_ranges
        self.max_weight = max_weight
        self.max_components = max_components

    def generate_parameters(self, pattern):
        if pattern in self.pattern_ranges:
            ranges = self.pattern_ranges[pattern]
            parameters = [random.uniform(r[0], r[1]) for r in ranges]
            
            # Apply weight constraint
            if pattern == 'Pattern1':
                parameters[0] = max(min(parameters[0], self.max_weight), -self.max_weight)
            
            # Apply component constraint
            parameters = parameters[:self.max_components]
            
            return tuple(parameters)
        else:
            return None

# Define pattern_ranges as a dictionary with keys as pattern names and values as lists of tuples containing the parameter ranges
pattern_ranges = {
    'Pattern1': [(-1, 1), (0, 1)],
    'Pattern2': [(0, 1), (0, 2 * math.pi)],
    'Pattern3': [(0, 1), (0, 1)],
    'Pattern4': [(0, 1), (0, 1), (0, 1)],
    'Pattern5': [(0, 1), (0, 1), (0, 1)],
}

# Instantiate the RandomParameterGenerator with limiting factors
random_parameter_generator = RandomParameterGenerator(pattern_ranges, max_weight=5, max_components=3)

# Use the generate_parameters method to generate random parameters for a given pattern
random_parameters = random_parameter_generator.generate_parameters('Pattern1')
