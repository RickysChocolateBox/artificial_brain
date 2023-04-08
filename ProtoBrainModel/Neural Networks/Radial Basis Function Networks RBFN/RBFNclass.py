import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from scipy.special import expit
from sklearn.linear_model import LinearRegression


class SimpleRBFN:
    def __init__(self, num_centers, num_classes):
        self.num_centers = num_centers
        self.num_classes = num_classes
        self.centers = None
        self.weights = None

    def _kernel_function(self, center, data_point, gamma=1):
        distance = np.sum((center - data_point) ** 2)
        return np.exp(-gamma * distance)

    def _calculate_interpolation_matrix(self, X):
        G = np.zeros((len(X), self.num_centers))

        for data_point_arg, data_point in enumerate(X):
            for center_arg, center in enumerate(self.centers):
                G[data_point_arg, center_arg] = self._kernel_function(center, data_point)

        return G
import numpy as np

class RBFN:
    def __init__(self, input_shape, num_centers, output_shape):
        self.input_shape = input_shape
        self.num_centers = num_centers
        self.output_shape = output_shape
        self.centers = None
        self.beta = None
        self.weights = None

    def _kernel_function(self, center, data_point):
        return np.exp(-self.beta * np.linalg.norm(center - data_point) ** 2)

    def _calculate_interpolation_matrix(self, X):
        G = np.zeros((len(X), self.num_centers))
        for data_point_arg, data_point in enumerate(X):
            for center_arg, center in enumerate(self.centers):
                G[data_point_arg, center_arg] = self._kernel_function(center, data_point)
        return G

    def _select_centers(self, X):
        random_args = np.random.choice(len(X), self.num_centers)
        centers = X[random_args]
        return centers

    def fit(self, X, Y):
        self.centers = self._select_centers(X)
        self.beta = 1 / (2 * (np.linalg.norm(self.centers) ** 2))
        G = self._calculate_interpolation_matrix(X)
        self.weights = np.linalg.pinv(G).dot(Y)

    def predict(self, X):
        G = self._calculate_interpolation_matrix(X)
        predictions = G.dot(self.weights)
        return predictions

# Example usage
input_shape = 10
num_centers = 20
output_shape = 2

rbfn = RBFN(input_shape, num_centers, output_shape)
