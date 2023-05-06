import csv


with open("csv_file/dataset_20.csv", newline="") as f:
    reader = csv.reader(f)
    header = [next(reader)]
    list_action_dataset_20 = [
        [row[0], int(row[1]), int(row[2])] for row in reader
    ]


def get_combinaison_by_iteration(liste_element):
    """
    Get best invest to set binary number for each combination actions.
    :param liste_element: list of actions
    :return: list of best action
    """
    list_combinaison = []
    number_element = len(liste_element)
    # number_bits_combinaison = number of possible combinations
    number_bits_combinaison = 2**number_element
    for i in range(number_bits_combinaison):
        # Convert i in binary number of length of list_element
        combinaison_bits = f"{i:0{number_element}b}"
        # convert string to number list
        int_combinaison = [int(x) for x in combinaison_bits]
        combinaison = []
        for idx, element in enumerate(int_combinaison):
            if element == 1:
                combinaison.append(liste_element[idx])
        if sum([x[1] for x in combinaison]) < 500:
            gain_total = sum([x[1] * x[2] / 100 for x in combinaison])
            combinaison.append(gain_total)
            list_combinaison.append(combinaison)

    return list_combinaison


def iteration(list_element):
    list_combinaison_iteration = get_combinaison_by_iteration(list_element)
    list_combinaison_sorted = sorted(list_combinaison_iteration, key=lambda x: x[-1])
    return list_combinaison_sorted


# Bruteforce by recursivity

# action mini = action with the lowest cost
action_mini = min([x[1] for x in list_action_dataset_20])

best_action = []


def get_combinaison_by_recursivity(actions_list, budget=500, liste=None):
    """
    Get best invest for each combination actions by recursivity.
    :param actions_list: actions list
    :param budget: 500 by default
    :param liste: empty list by default
    """
    if liste is None:
        liste = []
    for action in actions_list:
        # If budget - cost action > 0
        if budget - action[1] >= 0:
            info_action = [action[0], action[1], action[2]]
            remaining_budget = budget - action[1]
            liste.append(info_action)
            if len(liste) > 0:
                profit = sum([x[1] * x[2] / 100 for x in liste])
                copy_liste = liste.copy()
                copy_liste.append(profit)
                best_action.append(copy_liste)

            if remaining_budget >= action_mini:
                """
                recall get_combinaison_by_recursivity with
                :parameter actions_list :  actions_list without action
                :parameter budget : remaining_budget
                :parameter liste : liste
                """
                get_combinaison_by_recursivity(
                    actions_list=actions_list[actions_list.index(action) + 1:],
                    budget=remaining_budget,
                    liste=liste,
                )
                liste.pop()

            else:
                profit = sum([x[1] * x[2] / 100 for x in liste])
                copy_liste = liste.copy()
                copy_liste.append(profit)
                best_action.append(copy_liste)
                liste.pop()
        else:
            continue


def recursivity(actions_list, budget=500, liste=None):
    get_combinaison_by_recursivity(actions_list, budget, liste)
    best_action_sorted = sorted(best_action, key=lambda x: x[-1])
    return best_action_sorted


def print_result(function, name):
    best_invest = function
    print(
        f"Résultat avec la function {name.__name__}():\n"
        f"Meilleur investissement: {[x[0] for x in best_invest[-1][:-1]]}\n"
        f"Cout total: {sum([x[1] for x in best_invest[-1][:-1]])}€\n"
        f"Profit: {round(best_invest[-1][-1], 2)}€"
    )


print_result(recursivity(list_action_dataset_20), recursivity)
print_result(iteration(list_action_dataset_20), iteration)
