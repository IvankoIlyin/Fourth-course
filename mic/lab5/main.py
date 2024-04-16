import os
import tarfile
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

HOUSES_PATH = os.path.join("datasets", "houses")

full_pipeline = Pipeline([('std_scaler', StandardScaler())])


def load_houses_data(neo_path=HOUSES_PATH):
    csv_path = os.path.join("kc_house_data.csv")
    return pd.read_csv(csv_path)


houses = load_houses_data()

print(houses.head())

