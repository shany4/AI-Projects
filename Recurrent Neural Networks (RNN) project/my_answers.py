import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import LSTM
import keras


import string


def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    for i in range(0, len(series) - window_size):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size])

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y


def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))

    # optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
    # model.compile(loss='mean_squared_error', optimizer=optimizer)

    return model


def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    char = list(string.ascii_lowercase)
    good = set(punctuation + char + [' '])

    all = set(text)
    junk = all - good

    for i in junk:
        text = text.replace(i, ' ')

    return text


def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    for i in range(0, len(text) - window_size, step_size):
        inputs.append(text[i : i + window_size])
        outputs.append(text[i + window_size])

    return inputs,outputs


def build_part2_RNN(window_size, num_chars):

    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars))
    model.add(Activation('softmax'))

    # optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
    # model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model
