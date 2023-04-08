import numpy as np
import tensorflow as tf
from tensorflow import keras 
from keras import layers, models

class CNN:
    def __init__(self, input_shape, num_classes, conv_layers, dense_layers, dropout_rate=0.5, neurotransmitter_classes=None):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.conv_layers = conv_layers
        self.dense_layers = dense_layers
        self.dropout_rate = dropout_rate
        self.neurotransmitter_classes = neurotransmitter_classes if neurotransmitter_classes is not None else []
        self.model = self.build_model()

    def apply_neurotransmitter_effects(self, x_train, y_train):
        for neurotransmitter_class in self.neurotransmitter_classes:
            neurotransmitter = neurotransmitter_class()
            neurotransmitter.model = self.model
            neurotransmitter.train(x_train, y_train)

    def build_model(self):
        inputs = layers.Input(shape=self.input_shape)
        x = inputs

        for conv_layer in self.conv_layers:
            x = layers.Conv2D(conv_layer['filters'], conv_layer['kernel_size'], activation='relu')(x)
            if 'pool_size' in conv_layer:
                x = layers.MaxPooling2D(conv_layer['pool_size'])(x)

        x = layers.Flatten()(x)

        for dense_layer in self.dense_layers:
            x = layers.Dense(dense_layer, activation='relu')(x)
            x = layers.Dropout(self.dropout_rate)(x)

        outputs = layers.Dense(self.num_classes, activation='softmax')(x)

        return models.Model(inputs, outputs)

    def compile(self, optimizer, loss, metrics):
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def fit(self, x_train, y_train, batch_size, epochs, validation_data=None):
        self.apply_neurotransmitter_effects(x_train, y_train)
        self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=validation_data)

    def evaluate(self, x_test, y_test):
        return self.model.evaluate(x_test, y_test)
