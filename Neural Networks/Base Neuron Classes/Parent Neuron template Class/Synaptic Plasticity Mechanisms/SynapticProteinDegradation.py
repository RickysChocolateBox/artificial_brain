import numpy as np

class SynapticProteinDegradation:
    def __init__(self, num_neurons, initial_degradation=None, degradation_rate=0.01, activity_threshold=0.5):
        if initial_degradation is None:
            self.protein_degradation = np.ones(num_neurons)
        else:
            self.protein_degradation = initial_degradation
        self.degradation_rate = degradation_rate
        self.activity_threshold = activity_threshold

    def update_protein_degradation(self, activity_levels, connectivity_matrix):
        # Calculate the change in synaptic protein degradation based on activity levels and connectivity
        for i in range(len(activity_levels)):
            for j in range(len(activity_levels)):
                if connectivity_matrix[i, j] > 0:
                    if activity_levels[i] > self.activity_threshold:
                        self.protein_degradation[i] -= self.degradation_rate * connectivity_matrix[i, j]
                    else:
                        self.protein_degradation[i] += self.degradation_rate * connectivity_matrix[i, j]

        # Ensure the protein degradation stays within a valid range
        self.protein_degradation = np.clip(self.protein_degradation, 0, 1)

        return self.protein_degradation

