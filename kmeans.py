import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import math

def euclid_distance(p1, p2):
    return math.eucli

def choose_init_centroids(points, k):
    centroids = []
    centroids.append(points[0])

def main():
    data = pd.read_csv("/home/chanwoo/PycharmProjects/crawler/company_data.csv")
    data.fillna(0)
    data_no_ticker = data.iloc[:,1:]
 #   print(data_no_ticker)
    std_data = StandardScaler().fit_transform(data_no_ticker)

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(std_data)
    principal_df = pd.DataFrame(data = principal_components, columns=['pc1', 'pc2'])
    print(principal_df)
if __name__ == '__main__':
    main()

