import time

import psutil

import numpy as np


def decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        total_time = end - start
        return result, total_time

    return wrapper


def loop(data_list, function):
    array_time = []
    array_ram = []
    for i in range(1, 25, 1):
        x = function(data_list[:i])
        array_time.append(x[1])
        memory = psutil.virtual_memory()
        array_ram.append(memory[3] / 1000000000)
        print('nbr entree', i, "/ram:", memory[3] / 1000000000, "/time:", x[1])
        print(len(x[0]))
    return array_time, array_ram

