import os
import sklearn
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from graphviz import Source
from sklearn.tree import DecisionTreeClassifier, export_graphviz, plot_tree
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("seeds_dataset.txt",  sep="\s+", names=['Area', 'Perimeter', 'Compactness', 'Length of kernel', 'Width of kernel', 'Asymmetry coefficient',  'Length of kernel groove', 'Class'])
df = df.dropna()
print(df)


