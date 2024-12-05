from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Flatten, Dropout # type: ignore

# Example model
model = Sequential()
model.add(Flatten(input_shape=(28, 28, 2)))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.summary()
