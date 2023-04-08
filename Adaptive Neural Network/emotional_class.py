class EmotionalModel:
    def __init__(self, num_emotions, min_value=-1, max_value=1, emotion_decay_rate=0.1):
        self.emotional_state = [0] * num_emotions
        self.min_value = min_value
        self.max_value = max_value
        self.emotion_decay_rate = emotion_decay_rate

    def increase_emotion(self, emotion_index, value):
        self.emotional_state[emotion_index] = min(self.emotional_state[emotion_index] + value, self.max_value)

    def decrease_emotion(self, emotion_index, value):
        self.emotional_state[emotion_index] = max(self.emotional_state[emotion_index] - value, self.min_value)

    def decay_emotions(self):
        for i in range(len(self.emotional_state)):
            if self.emotional_state[i] > 0:
                self.emotional_state[i] -= self.emotion_decay_rate
            elif self.emotional_state[i] < 0:
                self.emotional_state[i] += self.emotion_decay_rate

            # Ensuring the emotional state stays within the allowed range
            self.emotional_state[i] = max(min(self.emotional_state[i], self.max_value), self.min_value)

