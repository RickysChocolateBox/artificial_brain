import numpy as np
import random

class EnsembleLearning:
    def __init__(self, num_models, model_class):
        self.num_models = num_models
        self.model_class = model_class
        self.models = [self.model_class() for i in range(num_models)]

    def fit(self, X, y):
        for model in self.models:
            indices = [random.randint(0, len(X) - 1) for i in range(len(X))]
            X_train = X[indices]
            y_train = y[indices]
            model.fit(X_train, y_train)

    def predict(self, X):
        predictions = []
        for model in self.models:
            predictions.append(model.predict(X))
        return np.mean(predictions, axis=0)

