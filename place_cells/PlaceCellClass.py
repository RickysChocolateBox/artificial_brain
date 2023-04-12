import tensorflow as tf
import numpy as np

class PlaceCellModel:
    def __init__(self, input_shape, num_place_cells):
        self.num_place_cells = num_place_cells
        self.place_cell_weights = tf.Variable(
            tf.random.normal((input_shape[1], num_place_cells))
        )
        self.place_cell_bias = tf.Variable(tf.zeros((num_place_cells,)))
        self.iterations = 0

    def process_input(self, input_data):
        place_cell_activity = tf.matmul(input_data, self.place_cell_weights)
        place_cell_activity = tf.nn.bias_add(place_cell_activity, self.place_cell_bias)
        place_cell_activity = tf.nn.relu(place_cell_activity)
        return place_cell_activity.numpy()

    def apply_hebbian_learning(self, place_cell_activity):
        delta_weights = tf.tensordot(place_cell_activity, place_cell_activity, axes=([0], [0]))
        delta_weights /= np.prod(place_cell_activity.shape)
        self.place_cell_weights += delta_weights

    def fractal_growth_iteration(self):
        self.iterations += 1
        new_place_cells = self.generate_fractal_place_cells(self.iterations)
        self.place_cell_weights = tf.concat([self.place_cell_weights, new_place_cells], axis=1)
        self.place_cell_bias = tf.concat(
            [self.place_cell_bias, tf.zeros((new_place_cells.shape[1],))], axis=0
        )
        self.num_place_cells += new_place_cells.shape[1]

    def generate_fractal_place_cells(self, iterations):
        new_place_cells = tf.random.normal(
            (self.place_cell_weights.shape[0], 2 ** iterations)
        )
        return new_place_cells
