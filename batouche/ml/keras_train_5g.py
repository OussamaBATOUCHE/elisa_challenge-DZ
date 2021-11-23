from tensorflow.keras import layers
from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)


url = 'ml/dataset/light_data.csv'
column_names = ['Idx2', 'Idx', 'Lon', 'Lat', 'Day', 'E']

raw_dataset = pd.read_csv(url, names=column_names,
                          na_values='?', comment='\t',
                          sep=',', skipinitialspace=True)

dataset = raw_dataset.copy()

dataset = dataset[1:].astype(
    {"Lon": float, "Lat": float, "Day": float, "E": float})
print(dataset.tail())

dataset.isna().sum()
dataset = dataset.dropna()
dataset.tail()


train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)


# train_dataset.describe().transpose()


train_features = train_dataset[['Lon', 'Lat', 'Day', 'E']].copy()
test_features = test_dataset[['Lon', 'Lat', 'Day', 'E']].copy()

train_labels = train_features.pop('E')
test_labels = test_features.pop('E')


# Normal
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))
print(normalizer.mean.numpy())


def build_and_compile_model(norm):
    model = keras.Sequential([
        norm,
        layers.Dense(60, activation='relu'),
        layers.Dense(60, activation='relu'),
        layers.Dense(1)
    ])

    model.compile(loss='mean_absolute_error',
                  optimizer=tf.keras.optimizers.Adam(0.001))
    return model


# Regression using a DNN and multiple inputs
dnn_model = build_and_compile_model(normalizer)
# dnn_model.summary()

history = dnn_model.fit(
    train_features,
    train_labels,
    validation_split=0.2,
    verbose=0, epochs=100)


def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error [E]')
    plt.legend()
    plt.grid(True)
    plt.show()


test_results = {}
plot_loss(history)

test_results['dnn_model'] = dnn_model.evaluate(
    test_features, test_labels, verbose=0)


# prediction():
test_predictions = dnn_model.predict(test_features).flatten()
a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [E]')
plt.ylabel('Predictions [E]')
lims = [0, 50]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)
plt.show()


# Save the model
# dnn_model.save('keras_dnn_model')

# reload
# reloaded = tf.keras.models.load_model('dnn_model')

# test_results['reloaded'] = reloaded.evaluate(
#     test_features, test_labels, verbose=0)
