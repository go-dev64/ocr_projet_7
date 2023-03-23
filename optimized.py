import pandas as pd

import numpy as np

dataset1 = pd.read_csv('csv_file/dataset1.csv')
dataset2 = pd.read_csv('csv_file/dataset2.csv')

dataset1["gain"] = round(dataset1['price'] * dataset1['profit'] / 100, 2)
dataset1_cleaned = dataset1.loc[(dataset1['price'] > 0) & (dataset1['price'] < 500) & (dataset1['profit'] > 0), :]

dataset2["gain"] = round(dataset2['price'] * dataset2['profit'] / 100, 2)
dataset2_cleaned = dataset2.loc[(dataset2['price'] > 0) & (dataset2['price'] < 500) & (dataset2['profit'] > 0), :]




data1 = np.asarray(dataset1_cleaned)
data2 = np.asarray(dataset2_cleaned)


def dynamique(budget, elements_list):
    # creation de la matrice vide
    matrice = np.zeros((len(elements_list) + 1, budget + 1))
    # pour chaque element
    for i in np.arange(1, len(elements_list) + 1):
        for w in np.arange(1, budget + 1):
            if elements_list[i - 1][1] <= w:
                matrice[i][w] = max(elements_list[i - 1][3] + matrice[i - 1][1], matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]

    w = budget
    n = len(elements_list)
    element_selection = []

    while w >= 0 and n >= 0:
        e = elements_list[n - 1]
        if matrice[n][w] == matrice[n - 1][w - int(e[1])] + int(e[3]):
            element_selection.append(e)
            w -= int(e[1])

        n -= 1

    return matrice[-1][-1], element_selection


#set1 = dynamique(500, data1)

set2 = dynamique(500, data2)
#print(set1)
print(set2)
