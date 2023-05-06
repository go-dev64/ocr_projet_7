import pandas as pd

import numpy as np

import math


def clean_csv(data, budget=500):
    """
    clean csv file -> remove elements which the value of cost
    and profit is lower than zero.
    create new column(index 3) -> gain = column[price] * column[profit] /100.
    create new column(index 4), convert column[price] (index 1) of float to int.
    :param data: csv file
    :param budget: int => budget by default = 500 euros
    :return: np.array
    """
    data["gain"] = round(data["price"] * data["profit"] / 100, 3)
    data["price_round"] = round(data["price"], 2) * 10
    data_cleaned = np.asarray(
        data.loc[
            (data["price"] > 0)
            & (data["price"] < budget * 10)
            & (data["profit"] > 0),
            :,
        ]
    )
    data_cleaned[:, 4] = np.ceil(data_cleaned[:, 4])
    return data_cleaned


def filter_data(data, budget, element_list):
    """
    returns the data for which the value of
    the column index 1(cost_action) is lower than the budget
    :param data:np.array
    :param budget: number
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


def get_best_profit(elements_list, budget=5000):
    """
    Dynamique programmation to determine the best actions association.
    First, to get best profit with matrix.
    Then, go through the matrix to get the stock with the best profit
    :param elements_list: list ->  actions list
    element_list[0] = action name,
    element_list[1] = action cost,
    element_list[2] = action profit,
    element_list[3] = action gain (element_list[1] * element_list[2] /100)
    element_list[4] = element_list[1] convert to int
    :param budget: number -> bu
    :return: profit max, actions list of best invest
    """
    matrice = np.zeros((len(elements_list) + 1, budget + 1))
    for i in np.arange(1, len(elements_list) + 1):
        for w in np.arange(1, budget + 1):
            # IF cost action  (i)<= slide of budget (w):
            if elements_list[i - 1][4] <= w:
                """matrix [i][w] = max between:
                the profit of the current action (i)
                + value of matrice at position w - cost of i.
                and
                matrix value at position [i-1][w]
                """
                matrice[i][w] = max(
                    elements_list[i - 1][3]
                    + matrice[i - 1][w - elements_list[i - 1][4]],
                    matrice[i - 1][w],
                )
            else:
                matrice[i][w] = matrice[i - 1][w]

    w = budget
    n = len(elements_list)
    element_selection = []
    while w >= 0 and n >= 0:
        element = elements_list[n - 1]
        """If matrix value at position[n][w] =
        matrix value at position[n - 1][w - cost element ] + profit element
        """
        if matrice[n][w] == matrice[n - 1][w - element[4]] + element[3]:
            element_selection.append(element)
            w -= element[4]
        n -= 1

    return matrice[-1][-1], element_selection


def print_result(list_action):
    """display results"""
    print(
        f"Meilleur investissement({len(list_action)} actions):\n"
        f"{[x[0] for x in list_action]}\n"
        f"Coût total: {round(sum([x[1] for x in list_action]), 2)}€\n"
        f"Profit: {round(sum([x[3] for x in list_action]), 2)}€"
    )


def get_best_invest(actions_list):
    best_invest = get_best_profit(actions_list)
    cost_best_invest = sum([x[1] for x in best_invest[1]])
    new_budget = 500 - cost_best_invest
    actions_list_filtered = filter_data(
        actions_list, budget=new_budget, element_list=best_invest[1]
    )
    if len(actions_list_filtered) > 0:
        list_action_new_budget = get_best_profit(
            actions_list_filtered, math.ceil(new_budget * 100)
        )
        final_action_list = np.append(
            best_invest[1],
            list_action_new_budget[1],
            axis=0
        )
        print_result(list_action=final_action_list)

    else:
        print_result(list_action=best_invest[1])


data1 = clean_csv(pd.read_csv("csv_file/dataset1.csv"))
data2 = clean_csv((pd.read_csv("csv_file/dataset2.csv")))
data20 = clean_csv(pd.read_csv("csv_file/dataset_24.csv"))

get_best_invest(data1)
get_best_invest(data2)
get_best_invest(data20)
