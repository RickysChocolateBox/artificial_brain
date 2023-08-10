import numpy as np

class SynapticTaggingAndCapture:
    def __init__(self, learning_rate, tag_lifetime, capture_threshold, noise_std_dev):
        self.learning_rate = learning_rate
        self.tag_lifetime = tag_lifetime
        self.capture_threshold = capture_threshold
        self.noise_std_dev = noise_std_dev

    # Decay function for tag values
    def decay_tag(self, tag_value):
        return tag_value * (1 - self.learning_rate)

    # Update function for the synaptic tag values
    def update_synaptic_tag(self, tag_value, activity_level):
        noise = np.random.normal(0, self.noise_std_dev)
        activity_level = 1 / (1 + np.exp(-(activity_level + noise)))
        if activity_level >= self.capture_threshold:
            tag_value += self.learning_rate
        tag_value = self.decay_tag(tag_value)
        return tag_value

