from bruteForce import list_action

liste_indices = list(range(len(list_action)))
list_combinaison = [{x} for x in liste_indices]
compteur = 0
total = 1
while total < 21:
    index = len(list_combinaison)
    for x in list_combinaison[compteur:index]:
        for y in liste_indices:
            if y in x:
                continue
            new_combinaison = x.copy()
            new_combinaison.add(y)
            if new_combinaison in list_combinaison[index:]:
                continue
            else:
                list_combinaison.append(new_combinaison)

    compteur = index
    total += 1

    """elif len(combinaison) < 21:
        break
    else:
        list_combinaison.append(combinaison)
        compteur += 1"""



print(list_combinaison)
print(len(list_combinaison))


