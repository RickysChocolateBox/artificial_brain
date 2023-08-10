import numpy as np

class DendriticSpineGrowthRetraction:
    def __init__(self, growth_rate, retraction_rate, growth_threshold, retraction_threshold,
                 max_spine_density, min_spine_density, learning_rate, noise_std_dev):
        self.growth_rate = growth_rate
        self.retraction_rate = retraction_rate
        self.growth_threshold = growth_threshold
        self.retraction_threshold = retraction_threshold
        self.max_spine_density = max_spine_density
        self.min_spine_density = min_spine_density
        self.learning_rate = learning_rate
        self.noise_std_dev = noise_std_dev

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def update_spine_density(self, spine_density, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = self.sigmoid(activity_level + noise)

        if activity_level >= self.growth_threshold:
            spine_density += self.learning_rate * self.growth_rate
        elif activity_level <= self.retraction_threshold:
            spine_density -= self.learning_rate * self.retraction_rate

        spine_density = np.clip(spine_density, self.min_spine_density, self.max_spine_density)
        return spine_density

