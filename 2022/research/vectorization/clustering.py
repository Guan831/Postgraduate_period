import pandas as pd
import requestForUrl
import numpy as np
import scipy
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram


def clustering(s):
    dataset = datasets.load_iris()
    dataset_data = dataset.data
    dataset_target = dataset.target
    target_names = dataset.target_names


if __name__ == '__main__':

    print()
