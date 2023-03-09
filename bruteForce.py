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


def get_combinaison(liste_des_actions, this_action, budget, liste):
    dictionnaire = {"name": this_action["name"]}

    # on calcule le reste = budget - cout action
    reste = budget - this_action["cout_par_action"]
    dictionnaire["reste"] = reste

    # calcule du benefice realise
    gain_action = this_action["cout_par_action"] * this_action["benefice"] / 100
    dictionnaire["gain_action"] = gain_action

    # on ajoute le dictionnaire à la liste des associations d'action
    liste.append(dictionnaire)

    # si reste different de 0 et supérieur au cout de l'action la plus base
    if reste >= action_mini:
        # copie de la liste des actions sans l'action en cours
        index = liste_des_actions.index(this_action)
        for j in liste_des_actions[index + 1:]:
            # on vérifie que le budget restant est divisible par l'action
            if reste - j["cout_par_action"] >= 0:
                # si ok → meme exercise mais avec le budget restant
                get_combinaison(liste_des_actions, budget=reste, this_action=j, liste=liste)
                liste.pop()

                # sinon on passe à l'élément suivant de la liste
            else:
                continue
    else:
        gain = get_gain_total(liste)
        copy_liste = liste.copy()
        copy_liste.append(gain)
        best_action.append(copy_liste)

for action in list_action:
    get_combinaison(liste_des_actions=list_action, budget=500, this_action=action, liste=[])


print(sorted(best_action, key=lambda combinaison: combinaison[-1])[-1])

