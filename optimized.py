import pandas as pd

import numpy as np

from utile import decorator


def clean_csv(data, budget=500):
    multiplicator = 10
    data["gain"] = round(data['price'] * data['profit'] / 100, 3)
    data["price"] = round(data["price"], 2) * multiplicator
    data_cleaned = np.asarray(
        data.loc[(data['price'] > 0) &
                 (data['price'] < budget * multiplicator) &
                 (data['profit'] > 0), :]
    )
    data_cleaned[:, 1] = np.ceil(data_cleaned[:, 1])
    return data_cleaned


data1 = clean_csv(pd.read_csv('csv_file/dataset1.csv'))
data2 = clean_csv((pd.read_csv('csv_file/dataset2.csv')))
data20 = clean_csv(pd.read_csv('csv_file/dataset_20.csv'))


def real_coast(actions_list_selected, data):
    real_invest = 0
    real_profit = 0
    list_index = []
    for v in actions_list_selected:
        for idx, i in enumerate(data):
            if v[0] == i[0]:
                list_index.append(idx)
                real_invest += i[1]
                real_profit += i[3]
    print(real_profit, real_invest, list_index)
    return real_invest, real_profit, list_index


@decorator
def dynamique(elements_list, budget=5000):
    # creation de la matrice vide
    matrice = np.zeros((len(elements_list) + 1, budget + 1))
    # pour chaque element de la liste (i):
    for i in np.arange(1, len(elements_list) + 1):
        # pour chaque tranche du budget (W)
        for w in np.arange(1, budget + 1):
            # Si, le cout de l'élément est ≤ à la tranche de prix
            if elements_list[i - 1][1] <= w:
                # On détermine le profit de l'élément actuel + celle de l'élément au cout précédent.
                # On garde le max et l'affecte à la position de la matrice pour i et w.
                matrice[i][w] = max(elements_list[i - 1][3] +
                                    matrice[i - 1][w - elements_list[i - 1][1]],
                                    matrice[i - 1][w])
            else:
                # Sinon on prend la valeur précédente comme valeur pour la position actuelle
                matrice[i][w] = matrice[i - 1][w]

    w = budget
    n = len(elements_list)
    element_selection = []
    # on parcourt tous les éléments de la matrice
    while w >= 0 and n >= 0:
        element = elements_list[n - 1]
        # Si la valeur de la matrice a la position [n][w] =
        # (matrice [n - 1][w - le cout de element ]) + valeur de element
        if matrice[n][w] == matrice[n - 1][w - element[1]] + element[3]:
            # alors on ajoute element à la liste
            element_selection.append(element)
            # on soustrait le cout de l'élément à
            w -= element[1]

        n -= 1

    real = real_coast(element_selection, elements_list)
    new_budget = budget - real[0]
    print(new_budget)
    if new_budget > 0:
        elements_list = np.delete(elements_list, real[2], 0)
        new_budget = budget - real[0]

        print(elements_list, len(elements_list))
        dynamique(elements_list, budget=budget - real[0] * 10)

    return matrice[-1][-1], element_selection


def print_result_dynamique(function):
    best_invest = function
    print(f"Meilleur investissement: {[x for x in best_invest[0][-1]]}\n"
          f"Cout total arrondi: {sum([x[1] / 10 for x in best_invest[0][-1]])}€\n"
          f"Profit round : {best_invest[0][0]}")


print_result_dynamique(dynamique(data1))
"""print_result_dynamique(dynamique(data2))
print_result_dynamique(dynamique(data20))"""
