list_action = [{"name": "Action-1", "cout_par_action": 20, "benefice": 5},
               {"name": "Action-2", "cout_par_action": 30, "benefice": 10},
               {"name": "Action-3", "cout_par_action": 50, "benefice": 15},
               {"name": "Action-4", "cout_par_action": 70, "benefice": 20},
               {"name": "Action-5", "cout_par_action": 60, "benefice": 17},
               {"name": "Action-6", "cout_par_action": 80, "benefice": 25},
               {"name": "Action-7", "cout_par_action": 22, "benefice": 7},
               {"name": "Action-8", "cout_par_action": 26, "benefice": 11},
               {"name": "Action-9", "cout_par_action": 48, "benefice": 13},
               {"name": "Action-10", "cout_par_action": 34, "benefice": 27},
               {"name": "Action-11", "cout_par_action": 42, "benefice": 17},
               {"name": "Action-12", "cout_par_action": 110, "benefice": 9},
               {"name": "Action-13", "cout_par_action": 38, "benefice": 23},
               {"name": "Action-14", "cout_par_action": 14, "benefice": 1},
               {"name": "Action-15", "cout_par_action": 18, "benefice": 3},
               {"name": "Action-16", "cout_par_action": 8, "benefice": 8},
               {"name": "Action-17", "cout_par_action": 4, "benefice": 12},
               {"name": "Action-18", "cout_par_action": 10, "benefice": 14},
               {"name": "Action-19", "cout_par_action": 24, "benefice": 21},
               {"name": "Action-20", "cout_par_action": 114, "benefice": 18}
               ]

action_mini = min([x["cout_par_action"] for x in list_action])


def get_gain_total(x):
    gain_total = 0
    for i in x:
        gain_total += i["gain_action"]
    return gain_total


best_action = []


def get_combinaison(liste_des_actions, budget, liste):
    budjet_restant = budget
    for action in liste_des_actions:
        if budjet_restant - action["cout_par_action"] >= 0:

            dictionnaire = {"name": action["name"]}

            # on calcule le reste = budget - cout action
            reste = budjet_restant - action["cout_par_action"]
            dictionnaire["reste"] = reste

            # calcule du benefice realise
            gain_action = action["cout_par_action"] * action["benefice"] / 100
            dictionnaire["gain_action"] = gain_action

            # on ajoute le dictionnaire à la liste des associations d'action
            liste.append(dictionnaire)

            # si reste different de 0 et supérieur au cout de l'action la plus base
            if reste >= action_mini:
                # copie de la liste des actions sans l'action en cours
                index = list_action.index(action)
                get_combinaison(liste_des_actions=list_action[index + 1:], budget=reste, liste=liste)
                liste.pop()
                # sinon on passe à l'élément suivant de la liste
            else:
                gain = get_gain_total(liste)
                copy_liste = liste.copy()
                copy_liste.append(gain)
                best_action.append(copy_liste)
                liste.pop()

        else:
            continue


get_combinaison(liste_des_actions=list_action, budget=500, liste=[])
print(sorted(best_action, key=lambda combinaison: combinaison[-1])[-1])
print(len(best_action))
