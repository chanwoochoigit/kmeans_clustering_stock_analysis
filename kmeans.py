import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import math

def euclid_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1]) * (p1[1]-p2[1]))

def choose_init_centroids(points, k):
    centroids = []
    centroids.append(points[0])

def get_optimal_k(data):
    sum_of_squared_distances = []
    # find out elbow
    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i)
        km = kmeans.fit(data)
        sum_of_squared_distances.append(km.inertia_)
    plt.plot(range(1, 10), sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('sum of squared distances')
    plt.title('Elbow to find k')
    plt.show()

def standardise(data):
    return StandardScaler().fit_transform(data)

def eliminate_nans(data):
    # replace nan values to zeros
    for row in data:
        for i in range(len(row)):
            if np.isnan(row[i]):
                row[i] = 0
    return data

def do_kmeans(data):
    km = KMeans(n_clusters=3)
    km.fit(data)
    p1 = data.iloc[:,0]
    p2 = data.iloc[:,1]
    labels=km.labels_
    print(labels)
    label_colour_dic = {0:'r', 1:'g', 2:'b'}
    label_colour = []
    for i in labels:
        label_colour.append(label_colour_dic.get(i))
    plt.scatter(p1, p2, c=label_colour)
    plt.show()

def main():

    data_csv = pd.read_csv("/home/chanwoo/PycharmProjects/crawler/company_data.csv")
    std_data = standardise(pd.DataFrame(data=data_csv.iloc[:,1:]))

    #Do pca in order to shrink the number of features
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(eliminate_nans(std_data))
    np.nan_to_num(principal_components)
    principal_df = pd.DataFrame(data = principal_components, columns=['pc1', 'pc2'])

    #print(principal_df)

    #get_optimal_k(principal_df)
    print(principal_df)
    do_kmeans(principal_df)

    exp = principal_df
    exp['ticker'] = data_csv['ticker']
    pd.set_option('display.max_columns', 500)
    print(exp)
if __name__ == '__main__':
    main()

