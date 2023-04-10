import tensorflow as tf
from tensorflow import keras
from keras import layers 
from keras import Input, Dense
from tensorflow import keras
from keras import models 
from keras import Model
from tensorflow import keras
from keras import optimizers 
from keras import Adam

# Define GABA model for Deep Belief Network
def GABA_DBN(input_shape):
    inputs = Input(shape=input_shape)
    x = Dense(256, activation='relu')(inputs)
    x = Dense(128, activation='relu')(x)
    x = Dense(64, activation='relu')(x)
    outputs = Dense(10, activation='softmax')(x)
    model = Model(inputs=inputs, outputs=outputs)
    
    # Compile the model with Adam optimizer and categorical crossentropy loss
    optimizer = Adam(lr=0.0001)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

