import keras 
from keras import layers, models

class ANN:
    def __init__(self, input_shape, hidden_layers, output_size, dopamine_ann, gaba_ann, norepinephrine_ann, serotonin_ann):
        self.input_shape = input_shape
        self.hidden_layers = hidden_layers
        self.output_size = output_size
        self.dopamine_ann = dopamine_ann
        self.gaba_ann = gaba_ann
        self.norepinephrine_ann = norepinephrine_ann
        self.serotonin_ann = serotonin_ann
        self.ann = self.build_ann(input_shape, hidden_layers, output_size)

    def build_ann(self, input_shape, hidden_layers, output_size):
        inputs = layers.Input(shape=input_shape)
        x = inputs

        for units in hidden_layers:
            x = layers.Dense(units, activation='relu')(x)
            x = layers.BatchNormalization()(x)
            x = layers.Dropout(0.5)(x)

        outputs = layers.Dense(output_size, activation='softmax')(x)

        return models.Model(inputs, outputs, name='ann')
