# --- IMPORT DEPENDENCIES --------------------------------------------------------------+
from tensorflow import keras
import data
import differential_evolution
import model
import sys
import datetime
# sys.stdout = open('TrainingsLog/train' +str(datetime.datetime.now().strftime("%Y%m%d%H%M"))+".log", 'w')

# --- PREPARE DATA ---------------------------------------------------------------------+
# dataset = data.preprocessing(
# "dataset/data_normalized.csv", "dataset/test.data", 0.8)

# --- META-HEURISTIQUE -----------------------------------------------------------------+
# best_model = differential_evolution.minimize(
#     dataset=dataset, popsize=4, maxiter=1)

# --- TRAIN & SAVE THE BEST MODEL ------------------------------------------------------+
# model.retrain_and_save(best_model, dataset, 20)

# --- END ------------------------------------------------------------------------------+


# Predict
# Load the model
# model = keras.models.load_model("best_model.h5")
# data_var = [[24.894964, 60.214456, 4]]  # 0.9000000000000001
# print("[Data for test] ", data_var)
# # Make prediction
# print(model.summary())
# pred = model.predict(data_var)
# result = pred[0][0]
# print(result)
