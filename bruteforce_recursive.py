from decorateur import decorator

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

            # si reste different de 0 et supérieur au cout de l'action la plus base
            if reste >= 4:
                # copie de la liste des actions sans l'action en cours
                index = list_action_dataset_20.index(action)
                get_combinaison(liste_des_actions=list_action_dataset_20[index + 1:], budget=reste, liste=liste)
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
def start(liste_des_actions, budget, liste):
    get_combinaison(liste_des_actions, budget, liste)
