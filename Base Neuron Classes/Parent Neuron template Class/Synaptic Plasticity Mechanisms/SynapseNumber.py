import numpy as np

def sigmoid(x, gain=1):
    return 1 / (1 + np.exp(-gain * x))

class SynapseNumber:
    def __init__(self, num_neurons, initial_number=None, growth_rate=0.01, decay_rate=0.005, activity_threshold=0.5, activity_sensitivity=1.0, min_synapses=0, max_synapses=np.inf, activation_function=sigmoid, learning_rate_growth=0.1, learning_rate_decay=0.1, pruning_threshold=0.01, noise_std=0.01, enable_growth=True, enable_decay=True):
        if initial_number is None:
            self.synapse_number = np.ones(num_neurons) * 10
        else:
            self.synapse_number = initial_number
        self.num_neurons = num_neurons
        self.growth_rate = growth_rate
        self.decay_rate = decay_rate
        self.activity_threshold = activity_threshold
        self.activity_sensitivity = activity_sensitivity
        self.min_synapses = min_synapses
        self.max_synapses = max_synapses
        self.activation_function = activation_function
        self.learning_rate_growth = learning_rate_growth
        self.learning_rate_decay = learning_rate_decay
        self.pruning_threshold = pruning_threshold
        self.noise_std = noise_std
        self.enable_growth = enable_growth
        self.enable_decay = enable_decay

    def update_synapse_number(self, pre_activity_levels, post_activity_levels, connectivity_matrix, synaptic_weights):
        # Add random noise to pre- and post-synaptic activity levels
        pre_activity_levels += np.random.normal(0, self.noise_std, size=pre_activity_levels.shape)
        post_activity_levels += np.random.normal(0, self.noise_std, size=post_activity_levels.shape)

        # Calculate the change in synapse number based on pre- and post-synaptic activity levels, connectivity, and synaptic weights
        for i in range(self.num_neurons):
            for j in range(self.num_neurons):
                if connectivity_matrix[i, j] > 0:
                    pre_synaptic_activity = self.activation_function(pre_activity_levels[i])
                    post_synaptic_activity = self.activation_function(post_activity_levels[j])
                    synapse_growth = pre_synaptic_activity * post_synaptic_activity * self.activity_sensitivity
                    
                    if synapse_growth > self.activity_threshold and self.enable_growth:
                        self.synapse_number[i] += self.growth_rate * connectivity_matrix[i, j] * synapse_growth
                        synaptic_weights[i, j] += self.learning_rate_growth * synapse_growth
                    elif self.enable_decay:
                        self.synapse_number[i] -= self.decay_rate * connectivity_matrix[i, j] * (1 - synapse_growth)
                        synaptic_weights[i, j] -= self.learning_rate_decay * (1 - synapse_growth)

                    # Prune synapses if their weight falls below the pruning threshold
                    if synaptic_weights[i, j] < self.pruning_threshold:
                        connectivity_matrix[i, j] = 0

        # Ensure the synapse number stays within a valid range
        self.synapse_number = np.clip(self.synapse_number, self.min_synapses, self.max_synapses)

        return self.synapse_number, connectivity_matrix, synaptic_weights

