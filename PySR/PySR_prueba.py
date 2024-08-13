
## Importando Librerias 
import numpy as np
import pandas as pd
from pysr import PySRRegressor
import matplotlib
import matplotlib.pyplot as plt

# importacion de DF
file_path = 'D:\\CODES\\ge_lab\\resources\\LIB\\CI\\df_cdrag_25.txt'
df_cdrag_25 = pd.read_csv(file_path, delimiter=',')

file_path = 'D:\\CODES\\ge_lab\\resources\\LIB\\CI\\df_cdrag_53.txt'
df_cdrag_53 = pd.read_csv(file_path, delimiter=',')

file_path = 'D:\\CODES\\ge_lab\\resources\\LIB\\CI\\df_cdrag_74.txt'
df_cdrag_74 = pd.read_csv(file_path, delimiter=',')

file_path = 'D:\\CODES\\ge_lab\\resources\\LIB\\CI\\df_cdrag_102.txt'
df_cdrag_102 = pd.read_csv(file_path, delimiter=',')

# definiendo conjunto de train
df_cdrag_train = pd.concat([df_cdrag_25, df_cdrag_74], ignore_index=True)

# separando entre x e y
y_train = df_cdrag_train['cdrag']
X_train = df_cdrag_train.drop(columns=['cdrag'])

# definiendo conjunto de test

y_test = df_cdrag_53['cdrag']
X_test = df_cdrag_53.drop(columns=['cdrag'])

# renombrando
X_train.rename(columns={'Rem':'ReyNum'}, inplace=True)
X_test.rename(columns={'Rem':'ReyNum'}, inplace=True)

# Modelo

model = PySRRegressor(
    niterations=200,
    binary_operators=["+", "-", "*", "/"],
    unary_operators=[],
    populations=200,
    population_size=20,
    verbosity=1,
    maxsize=12,
    parsimony=1e-3,
    progress=True
)

model.fit(X_train, y_train)
