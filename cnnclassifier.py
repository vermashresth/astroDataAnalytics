import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

training_set=pd.read_csv("/media/petrichor/data/bigdatafiles/kepler/exoTrain.csv")
X_train = training_set.iloc[:,1:].values
y_train = training_set.iloc[:,0:1].values

test_set=pd.read_csv("/media/petrichor/data/bigdatafiles/kepler/exoTest.csv")
X_test = test_set.iloc[:,1:].values
y_test = test_set.iloc[:,0:1].values

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


X_train = np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

from keras.models import Sequential
from keras.layers import Convolution1D
from keras.layers import MaxPooling1D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers.normalization import BatchNormalization




classifier = Sequential()
classifier.add(Convolution1D(filters=8, kernel_size=11, activation="relu", input_shape=(3197,1)))

classifier.add(MaxPooling1D(strides=4))
classifier.add(BatchNormalization())

classifier.add(Flatten())

classifier.add(Dropout(0.5))
classifier.add(Dense(64, activation='relu'))
classifier.add(Dropout(0.25))
classifier.add(Dense(64, activation='relu'))
classifier.add(Dense(1, activation='sigmoid'))

classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

classifier.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test,y_test))

score = classifier.evaluate(X_test, y_test)
print(score)
