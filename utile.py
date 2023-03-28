import time

import psutil


def decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        print("start")
        result = function(*args, **kwargs)
        end = time.time()
        print("stop")
        total_time = end - start
        print(f"temps excution = {total_time}")
        return result, total_time

    return wrapper


def loop(data_list, function, input_number):
    array_time = []
    array_ram = []
    array_input = []
    for i in range(1, input_number, 1):
        array_input.append(i)
        x = function(data_list[:i])
        array_time.append(x[1])
        memory = psutil.virtual_memory()
        array_ram.append(memory[3] / 1000000000)
        print('nbr entree', i, "/ram:", memory[3] / 1000000000, "/time:", x[1])
        print(len(x[0]))
    return array_time, array_ram, array_input


def print_result(function):
    best_invest = function
    print(f"Meilleur investissement: {[x[0] for x in best_invest[0][-1][:-1]]}\n"
          f"Cout total: {sum([x[1] for x in best_invest[0][-1]])}€\n"
          f"Profit: {round(best_invest[0][-1][-1], 2)}€")


def print_result_dynamique(function, data):
    best_invest = function
    profit = best_invest[0][0]
    somme = 0
    prpr = 0
    for v in best_invest[0][1]:
        for i in data:
            if v[0] == i[0]:
                somme += i[1]
                prpr += i[3]

    liste_meilleur_action = best_invest[0][1]
    print(len(liste_meilleur_action))
    print(f"Meilleur investissement: {[x[0] for x in best_invest[0][-1]]}\n"
          f"Cout total arrondi: {sum([x[1] / 10 for x in best_invest[0][1]])} / reel: {somme}€\n"
          f"Profit round : {round(profit, 2)}€ / profit verifier = {prpr} ")
