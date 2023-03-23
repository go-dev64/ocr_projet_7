import time

import psutil


def decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        total_time = end - start
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
          f"Cout total: {sum([x[1] for x in best_invest[0][-1][:-1]])}€\n"
          f"Profit: {round(best_invest[0][-1][-1], 2)}€")
