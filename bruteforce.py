import csv



from memory_profiler import profile

import matplotlib.pyplot as plt

from decorateur import decorator, loop

with open('csv_file/dataset_20.csv', newline='') as f:
    reader = csv.reader(f)
    header = [next(reader)]
    list_action_dataset_20 = [[row[0], int(row[1]), int(row[2])] for row in reader]



@decorator
def brute_force_binary(liste_element):
    # liste des différentes combinaison possible
    list_combinaison = []
    # on définit le nombre d'éléments dans la liste
    nombre_element = len(liste_element)
    # on calcule le nombre de combinaisons
    nombre_bits_combinaison = 2 ** nombre_element
    # pour chaque combinaison dans le nombre total de combinaison possible :
    for i in range(nombre_bits_combinaison):
        # on convertit le nombre i en nombre binaire de longueur de là du nombre d'éléments longueur du tableau
        combinaison_bits = f"{i:0{nombre_element}b}"
        # on convertit le string en list d'entier 0 et
        int_combinaison = [int(x) for x in combinaison_bits]
        # on associe chaque element à l'index du tableau d'action.
        combinaison = []
        for idx, element in enumerate(int_combinaison):
            # si i = 1 , alors l'index de i  = list_action[index de i]
            if element != 0:
                # on ajoute l'action dans la combinaison
                combinaison.append(liste_element[idx])
        # on ajoute la combinaison dans la liste des combinaisons : Si :
        # Si le nombre élément de la combinaison est supérieur à 2) et la somme du cout action :
        if sum([x[1] for x in combinaison]) < 500:
            # on calcule le gain total de la combinaison
            gain_total = sum([x[1] * x[2] / 100 for x in combinaison])
            combinaison.append(gain_total)
            # alors on ajoute la combinaison dans la liste des combinaisons
            list_combinaison.append(combinaison)
    list_combinaison_sorted = sorted(list_combinaison, key=lambda x: x[-1])
    return list_combinaison_sorted


# Génére la Liste des meilleures actions par récursivité
action_mini = min([x[1] for x in list_action_dataset_20])

best_action = []


def get_combinaison(liste_des_actions, budget=500, liste=None):
    if liste is None:
        liste = []
    budget_restant = budget
    for action in liste_des_actions:
        if budget_restant - action[1] >= 0:

            dictionnaire = {"name": action[0]}

            # on calcule le reste = budget - cout action
            reste = budget_restant - action[1]
            dictionnaire["reste"] = reste

            # calcule du benefice realise
            gain_action = action[1] * action[2] / 100
            dictionnaire["gain_action"] = gain_action

            # on ajoute le dictionnaire à la liste des associations d'action
            liste.append(dictionnaire)
            if len(liste) > 0:
                gain = sum([x["gain_action"] for x in liste])
                copy_liste = liste.copy()
                copy_liste.append(gain)
                best_action.append(copy_liste)

            # si reste different de 0 et supérieur au cout de l'action la plus base
            if reste >= 4:
                # copie de la liste des actions sans l'action en cours
                index = liste_des_actions.index(action)
                get_combinaison(liste_des_actions=liste_des_actions[index + 1:], budget=reste, liste=liste)
                liste.pop()
                # sinon on passe à l'élément suivant de la liste
            else:
                gain = sum([x["gain_action"] for x in liste])
                copy_liste = liste.copy()
                copy_liste.append(gain)
                best_action.append(copy_liste)
                liste.pop()

        else:
            continue


@decorator
def start(liste_des_actions, budget=500, liste=None):
    get_combinaison(liste_des_actions, budget, liste)
    best_action_sorted = sorted(best_action, key=lambda x: x[-1])
    return best_action_sorted


array_recursive = loop(list_action_dataset_20, start)
array_binary = loop(list_action_dataset_20, brute_force_binary)
temps = [x for x in range(1, 21)]
"""
plt.plot(temps, array_recursive, label='bruteForce récursif', color='blue')
plt.plot(temps, array_binary, label='bruteForce iteratif', color='green')
plt.legend()
plt.show()"""
