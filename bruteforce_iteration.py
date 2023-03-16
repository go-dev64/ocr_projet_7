from decorateur import decorator


"""
with open('csv_file/dataset_20.csv', newline='') as f:
    reader = csv.reader(f)
    header = [next(reader)]
    list_action_dataset_20 = [[row[0], int(row[1]), int(row[2])] for row in reader]"""


@decorator
def bin_function(liste_element):
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
        if sum([x[1] for x in combinaison]) < 500 and len(combinaison) > 2:
            # on calcule le gain total de la combinaison
            gain_total = sum([x[1] * x[2] / 100 for x in combinaison])
            combinaison.append(gain_total)
            # alors on ajoute la combinaison dans la liste des combinaisons
            list_combinaison.append(combinaison)
    list_combinaison_sorted = sorted(list_combinaison, key=lambda x: x[-1])
    return list_combinaison_sorted
