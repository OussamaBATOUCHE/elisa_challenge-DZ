# --- IMPORT DEPENDENCIES --------------------------------------------------------------+
import data
import differential_evolution
import model
import sys
import datetime
sys.stdout = open('TrainingsLog/train' +
                  str(datetime.datetime.now().strftime("%Y%m%d%H%M"))+".log", 'w')

# --- PREPARE DATA ---------------------------------------------------------------------+
dataset = data.preprocessing(
    "dataset/data_normalized.csv", "dataset/test.data", 0.8)

# --- META-HEURISTIQUE -----------------------------------------------------------------+
# best_model = differential_evolution.minimize(
#     dataset=dataset, popsize=3, maxiter=2)

# --- TRAIN & SAVE THE BEST MODEL ------------------------------------------------------+
# model.retrain_and_save(best_model, dataset, 20)

# --- END ------------------------------------------------------------------------------+
