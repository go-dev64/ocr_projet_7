import csv

with open('csv_file/dataset_24.csv', newline='') as f:
    reader = csv.reader(f)
    header = [next(reader)]
    list_action_dataset_20 = [[row[0], int(row[1]), int(row[2])] for row in reader]


def get_combinaison_by_iteration(liste_element):
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
        # on convertit le string en list d'entier 0 et 1.
        int_combinaison = [int(x) for x in combinaison_bits]
        # on associe chaque element à l'index du tableau d'action.
        combinaison = []
        for idx, element in enumerate(int_combinaison):
            # si i = 1 , alors l'index de i  = list_action[index de i]
            if element != 0:
                # on ajoute l'action dans la combinaison
                combinaison.append(liste_element[idx])
        # on ajoute la combinaison dans la liste des combinaisons : Si :
        # Si la somme du cout action :
        if sum([x[1] for x in combinaison]) < 500:
            # on calcule le gain total de la combinaison
            gain_total = sum([x[1] * x[2] / 100 for x in combinaison])
            combinaison.append(gain_total)
            # alors on ajoute la combinaison dans la liste des combinaisons
            list_combinaison.append(combinaison)

    return list_combinaison


def iteration(list_element):
    list_combinaison_iteration = get_combinaison_by_iteration(list_element)
    # tri de la liste par rapport au profit généré
    list_combinaison_sorted = sorted(list_combinaison_iteration, key=lambda x: x[-1])
    return list_combinaison_sorted


# Bruteforce par récursivité

# action mini = action avec le cout le plus faible
action_mini = min([x[1] for x in list_action_dataset_20])

best_action = []


def get_combinaison_by_recursivity(liste_des_actions, budget=500, liste=None):
    if liste is None:
        # liste où l'on stockera les combinaisons d'actions
        liste = []
    budget_restant = budget
    for action in liste_des_actions:
        # on soustrait le cout de l'action au budget, et si >= 0
        if budget_restant - action[1] >= 0:
            # on stocke l'info de l'action en cours dans une liste
            info_action = [action[0], action[1], action[2]]

            # on calcule le reste = budget - cout action
            reste = budget_restant - action[1]
            # on ajoute la liste contenant les infos de l'action en cours
            # à la liste des combinaisons d'action.
            liste.append(info_action)
            if len(liste) > 0:
                gain = sum([x[1] * x[2] / 100 for x in liste])
                copy_liste = liste.copy()
                copy_liste.append(gain)
                best_action.append(copy_liste)

            # si reste different de 0 et supérieur au cout de l'action la plus base
            if reste >= 4:
                # copie de la liste des actions sans l'action en cours

                get_combinaison_by_recursivity(
                    liste_des_actions=liste_des_actions[liste_des_actions.index(action) + 1:],
                    budget=reste,
                    liste=liste)
                liste.pop()
                # sinon on passe à l'élément suivant de la liste
            else:
                # calcule du gain total de la combinaison d'action
                gain = sum([x[1] * x[2] / 100 for x in liste])
                # copie de celle-ci
                copy_liste = liste.copy()
                # ajout du gain a la copie
                copy_liste.append(gain)
                # on ajoute la copie à la liste des meilleures actions
                best_action.append(copy_liste)
                liste.pop()
        else:
            continue


def recursivity(liste_des_actions, budget=500, liste=None):
    get_combinaison_by_recursivity(liste_des_actions, budget, liste)
    # tri de la liste par rapport au profit généré
    best_action_sorted = sorted(best_action, key=lambda x: x[-1])
    return best_action_sorted


def print_result(function, name):
    best_invest = function
    print(f"Résultat avec la function {name.__name__}():\n"
          f'    Meilleur investissement: {[x[0] for x in best_invest[-1][:-1]]}\n'
          f'    Cout total: {sum([x[1] for x in best_invest[-1][:-1]])}€\n'
          f'    Profit: {round(best_invest[-1][-1], 2)}€')


"""print_result(recursivity(list_action_dataset_20), recursivity)
print_result(iteration(list_action_dataset_20), iteration)"""
