import numpy as np
import random
from sklearn.metrics import hinge_loss, log_loss, mean_absolute_error, mean_squared_error, mean_squared_log_error, log_loss
from scipy.spatial.distance import cosine
from hyperopt import fmin, tpe, hp

class OptimizationAlgorithmBaseClass:
    def __init__(self):
        self.gradient_objective_functions = {
            'mean_squared_error': self.mean_squared_error,
            'binary_crossentropy': self.binary_crossentropy,
            'categorical_crossentropy': self.categorical_crossentropy,
            'sparse_categorical_crossentropy': self.sparse_categorical_crossentropy,
            'hinge_loss': self.hinge_loss,
            'squared_hinge_loss': self.squared_hinge_loss,
            'huber_loss': self.huber_loss,
            'log_cosh_loss': self.log_cosh_loss,
            'poisson_loss': self.poisson_loss,
            'kullback_leibler_divergence': self.kullback_leibler_divergence,
            'multi_label_margin_loss': self.multi_label_margin_loss,
            'cosine_proximity_loss': self.cosine_proximity_loss
        }
        self.auto_select_gradient_objective_function()
def update_weights(self, weights, gradients):
        raise NotImplementedError("update_weights method should be implemented by subclasses.")
def auto_select_gradient_objective_function(self):
        # Randomly select a gradient objective function
        self.selected_gradient_objective_function = random.choice(list(self.gradient_objective_functions.keys()))

def mean_squared_error(self, y_true, y_pred):
        return mean_squared_error(y_true, y_pred)

def binary_crossentropy(self, y_true, y_pred):
        return log_loss(y_true, y_pred)

def categorical_crossentropy(self, y_true, y_pred):
        return log_loss(y_true, y_pred, labels=np.unique(y_true))

def sparse_categorical_crossentropy(self, y_true, y_pred):
        y_true_sparse = np.zeros_like(y_pred)
        y_true_sparse[np.arange(len(y_true)), y_true.astype(int)] = 1
        return log_loss(y_true_sparse, y_pred, labels=np.unique(y_true_sparse))

def hinge_loss(self, y_true, y_pred):
        return hinge_loss(y_true, y_pred)

def squared_hinge_loss(self, y_true, y_pred):
        return np.mean(np.square(np.maximum(1 - y_true * y_pred, 0)))

def huber_loss(self, y_true, y_pred, delta=1.0):
        error = y_true - y_pred
        abs_error = np.abs(error)
        return np.mean(np.where(abs_error < delta, 0.5 * np.square(error), delta * (abs_error - 0.5 *delta)))

def log_cosh_loss(self, y_true, y_pred):
        error = y_true - y_pred
        return np.mean(np.log(np.cosh(error)))

def poisson_loss(self, y_true, y_pred):
        return np.mean(y_pred - y_true * np.log(y_pred))

def kullback_leibler_divergence(self, y_true, y_pred):
        return np.sum(y_true * np.log(y_true / (y_pred + 1e-7)), axis=-1).mean()

def multi_label_margin_loss(self, y_true, y_pred):
        y_pred_sorted = np.sort(y_pred, axis=-1)
        y_true_sorted = np.sort(y_true, axis=-1)
        return np.mean(np.sum(np.maximum(0, 1 - y_pred_sorted[:-1] + y_pred_sorted[1:]) * y_true_sorted[:-1], axis=-1))

def cosine_proximity_loss(self, y_true, y_pred):
        return cosine(y_true, y_pred)
class HyperParameterOptimizer:
    def __init__(self, optimizer_algorithm, search_space, objective_function, max_evals):
        self.optimizer_algorithm = optimizer_algorithm
        self.search_space = search_space
        self.objective_function = objective_function
        self.max_evals = max_evals

    def optimize(self):
        trials = Trials()
        fmin_fn = fmin(self.objective_function, self.search_space, algo=self.optimizer_algorithm, max_evals=self.max_evals, trials=trials)
        return fmin_fn, trials



    search_space = {
        'learning_rate': hp.loguniform('learning_rate', np.log(0.0001), np.log(0.1)),
        'batch_size': hp.choice('batch_size', [32, 64, 128]),
        'num_layers': hp.choice('num_layers', [1, 2, 3]),
        'num_neurons': hp.quniform('num_neurons', 32, 256, 32),
        'activation': hp.choice('activation', ['relu', 'sigmoid', 'tanh']),
        'optimizer': hp.choice('optimizer', ['sgd', 'adam', 'rmsprop']),
    }

    optimizer_algorithm = tpe.suggest
    max_evals = 50

    hyper_param_optimizer = HyperParameterOptimizer(optimizer_algorithm, search_space, objective_function, max_evals)
    best_params, trials = hyper_param_optimizer.optimize()

    print("Best Parameters: ", best_params)
    print("Best Validation Accuracy: ", -trials.best_trial['result']['loss'])
