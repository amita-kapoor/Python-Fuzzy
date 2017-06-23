import numpy as np
from keras.utils import np_utils
import tensorflow as tf
#tf.python.control_flow_ops = tf

# Set random seed
np.random.seed(42)

# Our data
X = np.array([[0,0],[0,1],[1,0],[1,1]]).astype('float32')
y = np.array([[0],[1],[1],[0]]).astype('float32')

# Initial Setup for Keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten

# One-hot encoding the output
y = np_utils.to_categorical(y)
print (y)

# Building the model
xor = Sequential()
# Hint: This next line is where you can change the number of neurons in the first hidden layer, it's current value is 8
#xor.add(Flatten(input_shape=(3, 2)))  Will convert 3x2 input to 1x6
xor.add(Dense(10, input_dim=2))
# Hint: This next line is where you can change the activation funcion to "relu"
xor.add(Activation("relu"))
xor.add(Dense(2))
xor.add(Activation("sigmoid"))

xor.compile(loss="categorical_crossentropy", optimizer="adam", metrics = ['accuracy'])

# Uncomment this line to print the model architecture
xor.summary()

# Fitting the model
# Hint: This next line is where you can change the number of epochs, it's set to 10 now.
history = xor.fit(X, y, nb_epoch=100, verbose=0)

# Scoring the model
score = xor.evaluate(X, y)
print("\nAccuracy: ", score[-1])

# Checking the predictions
print("\nPredictions:")
print(xor.predict_proba(X))
