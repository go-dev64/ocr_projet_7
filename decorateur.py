import time


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
    for i in range(int(len(data_list)/10), len(data_list) + 1, int(len(data_list)/10)):
        x = function(data_list[:i])
        array_time.append((i, x[1]))
    print(array_time)
    return array_time

