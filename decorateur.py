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


def loop(data_list, function):
    array_time = []
    for i in range(1, 21):
        x = function(data_list[:i])
        array_time.append(x[1])
        memory = psutil.virtual_memory()
        print('RAM dispo(Gb):', memory[1] / 1000000000, 'ram utilisé en Gb', memory[3]/ 1000000000 , memory[0]/ 1000000000 )
    print(array_time)

    return array_time

