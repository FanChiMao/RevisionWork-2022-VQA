import csv
import os
import pandas as pd
from sklearn import preprocessing

def read_KoNViD(data):
    min_max_scaler = preprocessing.MinMaxScaler()
    dmos_data = pd.read_csv(data)
    dmos_data = dmos_data.iloc[:, 1].values
    dmos_data = dmos_data.reshape(-1, 1)
    output = min_max_scaler.fit_transform(dmos_data)
    return output


if __name__ == '__main__':
    min_max_scaler = preprocessing.MinMaxScaler()
    path = 'E:/VQA Database/KoNViD_1k/KoNViD_1k_mos_delete_one.csv'
    csv_data = pd.read_csv(path)
    csv_data = csv_data.iloc[:, 1].values.reshape(-1, 1)
    data = min_max_scaler.fit_transform(csv_data)
    a = 1


