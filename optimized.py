import pandas as pd

import numpy as np

dataset1 = pd.read_csv('csv_file/dataset1.csv')
dataset2 = pd.read_csv('csv_file/dataset2.csv')

dataset1["gain"] = round(dataset1['price'] * dataset1['profit'] / 100, 2)
dataset1_cleaned = dataset1.loc[(dataset1['price'] > 0) & (dataset1['price'] < 500) & (dataset1['profit'] > 0), :]

dataset2["gain"] = round(dataset2['price'] * dataset2['profit'] / 100, 2)
dataset2_cleaned = dataset2.loc[(dataset2['price'] > 0) & (dataset2['price'] < 500) & (dataset2['profit'] > 1), :]

data1 = np.asarray(dataset1_cleaned)

data2 = np.asarray(dataset2_cleaned.sort_values("price", ascending=True))





def dynamique(budget, elements_list):
    # creation de la matrice vide
    matrice = np.zeros((len(elements_list) + 1, budget + 1))
    # pour chaque element
    for i in np.arange(1, len(elements_list) + 1):
        for w in np.arange(1, budget + 1):
            if elements_list[i - 1][1] <= w:
                matrice[i][w] = max(elements_list[i-1][3] + matrice[i-1][w-elements_list[i-1][1]], matrice[i-1][w])
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
#print(set1)
#set2 = dynamique(500, data2)

def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            print(elements[i-1][1])
            if elements[i-1][1] <= w:
                print(f" element[i-1][2] = {elements[i-1][2]}")
                print(f"matrice[i-1][w-elements[i-1][1]] = {matrice[i-1][w-elements[i-1][1]]}")
                print(f"matrice[i-1][w] = {matrice[i-1][w]}")
                print(f"max = {max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])}")
                #matrice indece actuelle = max entre :
                 # la valeur de element precedent + la valeur de la case de la matrice ligne i - 1, colone w actuelle - cout de l element prévedent
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection

ele = [('Montre à gousset', 2, 6),
        ('Boule de bowling', 3, 10),
        ('Portrait de tata Germaine', 4, 12)]

print('Algo dynamique', sacADos_dynamique(5, ele))


