import pandas as pd

import numpy as np

import math

from utile import decorator


def clean_csv(data, budget=500):
    """
    clean csv file -> remove elements which the value of cost and profit is lower than zero.
    create new column ( index 3) -> gain = column[price] * column[profit] /100
    crete new column (index 4) -> round price = round(data["price"], 2) *10
    :param data: csv file
    :param budget: int => budget by default = 500 euros
    :return: np.array
    """
    data["gain"] = round(data['price'] * data['profit'] / 100, 3)
    data["price_round"] = round(data["price"], 2) * 10
    data_cleaned = np.asarray(
        data.loc[(data['price'] > 0) &
                 (data['price'] < budget * 10) &
                 (data['profit'] > 0), :]
    )
    data_cleaned[:, 4] = np.ceil(data_cleaned[:, 4])
    return data_cleaned


def filter_data(data, budget, element_list):
    """
    returns the data for which the value of the column index 1 (cost_action) is lower than the budget
    :param data:np.array
    :param budget: number -> remaining budget = initial budget - total cost of element_list
    :param element_list: list of action selected
    :return: np.array
    """
    data_filtered = data[data[:, 1] <= budget]
    data_filtered[:, 4] = np.ceil(data_filtered[:, 1] * 100)
    name_list = [x[0] for x in element_list]
    indices_list = []
    for idx, i in enumerate(data_filtered):
        if i[0] in name_list:
            indices_list.append(idx)
    data_filtered = np.delete(data_filtered, indices_list, axis=0)
    return data_filtered


data1 = clean_csv(pd.read_csv('csv_file/dataset1.csv'))
data2 = clean_csv((pd.read_csv('csv_file/dataset2.csv')))
data20 = clean_csv(pd.read_csv('csv_file/dataset_24.csv'))


def get_best_invest(elements_list, budget=5000):
    """
    Dynamique programmation to determine the best actions association.
    :param elements_list: list ->  actions list
    :param budget: number -> budget max
    :return: profit max, actions list of best invest
    """
    # creation de la matrice vide
    matrice = np.zeros((len(elements_list) + 1, budget + 1))
    # pour chaque element de la liste (i):
    for i in np.arange(1, len(elements_list) + 1):
        # pour chaque tranche du budget (W)
        for w in np.arange(1, budget + 1):
            # Si, le cout de l'élément est ≤ à la tranche de prix
            if elements_list[i - 1][4] <= w:
                # On détermine le profit de l'élément actuel + celle de l'élément au cout précédent.
                # On garde le max et l'affecte à la position de la matrice pour i et w.
                matrice[i][w] = max(elements_list[i - 1][3] +
                                    matrice[i - 1][w - elements_list[i - 1][4]],
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
        if matrice[n][w] == matrice[n - 1][w - element[4]] + element[3]:
            # alors on ajoute element à la liste
            element_selection.append(element)
            # on soustrait le cout de l'élément à
            w -= element[4]
        n -= 1

    return matrice[-1][-1], element_selection


def print_result(list_action):
    """ display results"""
    print(f"Meilleur investissement({len(list_action)} actions):\n"
          f"{[x[0] for x in list_action]}\n"
          f"Cout total: {round(sum([x[1] for x in list_action]), 2)}€\n"
          f"Profit: {round(sum([x[3] for x in list_action]), 2)}€")


def print_result_dynamique(actions_list):
    best_invest = get_best_invest(actions_list)
    cost_best_invest = sum([x[1] for x in best_invest[1]])
    new_budget = 500 - cost_best_invest
    actions_list_filtered = filter_data(actions_list, budget=new_budget, element_list=best_invest[1])
    if len(actions_list_filtered) > 0:
        list_action_new_budget = get_best_invest(actions_list_filtered, math.ceil(new_budget * 100))
        final_action_list = np.append(best_invest[1], list_action_new_budget[1], axis=0)
        print_result(list_action=final_action_list)

    else:
        print_result(list_action=best_invest[1])


"""print_result_dynamique(data1)
print_result_dynamique(data2)
print_result_dynamique(data20)"""
