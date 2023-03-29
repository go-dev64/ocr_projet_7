import pandas as pd

import math

import numpy as np

from utile import decorator, print_result_dynamique



def clean_csv(data):
    data["gain"] = round(data['price'] * data['profit'] / 100, 2)
    data["price"] = round(data["price"], 2) * 10

    data_cleaned = np.asarray(
        data.loc[(data['price'] > 0) &
                 (data['price'] < 500 * 100) &
                 (data['profit'] > 0), :]
    )
    return data_cleaned


data1 = clean_csv(pd.read_csv('csv_file/dataset1.csv'))
data2 = clean_csv((pd.read_csv('csv_file/dataset2.csv')))
data_verif = pd.read_csv('csv_file/dataset1.csv')
data_verif["gain"] = data_verif['price'] * data_verif['profit'] / 100
data2cleaned = np.asarray(
    data_verif)
              data2_verif = pd.read_csv('csv_file/dataset2.csv')
              data2_verif["gain"] = data2_verif['price'] * data2_verif['profit'] / 100
data2_verif = np.asarray(data2_verif)


@decorator
def dynamique(budget, elements_list):
    # creation de la matrice vide
    matrice = np.zeros((len(elements_list) + 1, budget + 1))
    # pour chaque element de la liste (i):
    for i in np.arange(1, len(elements_list) + 1):
        # pour chaque tranche du budget (W)
        for w in np.arange(1, budget + 1):
            # Si, le cout de l'élément est <= à la tranche de prix
            if elements_list[i - 1][1] <= w:
                # on détermine le profit de l'élément actuel + celle de l'élément au cout précédent.
                # On garde le max et l'affecte à la position de la matrice pour i et w.
                matrice[i][w] = max(elements_list[i - 1][3] +
                                    matrice[i - 1][math.ceil(w - elements_list[i - 1][1])],
                                    matrice[i - 1][w])
            else:
                # Sinon on prend la valeur précédente comme valeur pour la position actuelle
                matrice[i][w] = matrice[i - 1][w]

    w = budget
    n = len(elements_list)
    element_selection = []
    # on parcours tous les éléments de la matrice
    while w >= 0 and n >= 0:
        element = elements_list[n - 1]
        # Si la valeur de la matrice a la position [n][w] =
        # (matrice [n - 1][w - le cout de element ]) + valeur de element
        if matrice[n][w] == matrice[n - 1][math.ceil(w - element[1])] + element[3]:
            # alors on ajoute element a la liste
            element_selection.append(element)
            # on soustrait le cout de l'élément à w
            w -= math.ceil(element[1])

        n -= 1

    return matrice[-1][-1], element_selection


print_result_dynamique(dynamique(5000, data1), data2cleaned)
