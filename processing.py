import pandas as pd 
import numpy as np 
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# import dataset
data = pd.read_csv('data_attackv5.csv', sep =',')
X = data.drop('label', axis=1)
y = data['label']

X_test = X.sample(frac=0.4)
y_test = keras.utils.to_categorical(y.loc[X_test.index].values, num_classes=5)

X_train = X.drop(X_test.index)
y_train = keras.utils.to_categorical(y.loc[X_train.index].values, num_classes=5)

X_test = X_test.values
X_train = X_train.values

#creating the model
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X.shape[1]))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(X_train, y_train,epochs=10)

score = model.evaluate(X_test, y_test)

print(score)