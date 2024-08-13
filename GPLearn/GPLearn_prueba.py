
# importando librerias

import matplotlib 
from gplearn.genetic import SymbolicRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils.random import check_random_state
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#import graphviz
import pandas as pd

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


 
# Modelo
est_gp = SymbolicRegressor(population_size=10000,
                           generations=200, stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05, p_point_mutation=0.1,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.005, random_state=0)

est_gp.fit(X_train, y_train)

print(est_gp._program)
