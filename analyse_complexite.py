import matplotlib.pyplot as plt

import pandas as pd

from bruteforce import list_action_dataset_20, recursivity, iteration

from test import print_result_dynamique, clean_csv

from utile import loop

import math


data_20_clean = clean_csv(pd.read_csv('csv_file/dataset_24.csv'))
data1 = clean_csv(pd.read_csv('csv_file/dataset1.csv'))
array_dynamique = loop(data_20_clean, print_result_dynamique,  24, 1)
array_recursive = loop(list_action_dataset_20, recursivity, 24, 1)
array_binary = loop(list_action_dataset_20, iteration, 24, 1)



plt.plot(array_recursive[2], array_recursive[0], label='bruteForce récursif', color='blue')
plt.plot(array_binary[2], array_binary[0], label='bruteForce itératif', color='green')
"""plt.plot(array_dynamique[2], array_dynamique[0], label='Optimized', color='orange')"""
plt.xlabel('nombre entrée')
plt.ylabel('temps execution (s)')
plt.legend()
plt.show()

plt.plot(array_recursive[2], array_recursive[1], label='bruteForce récursif', color='blue')
plt.plot(array_binary[2], array_binary[1], label='bruteForce itératif', color='green')
"""plt.plot(array_dynamique[2], array_dynamique[1], label='Optimized', color='orange')"""
plt.xlabel('nombre entrée')
plt.ylabel('Ram utilisée (Go)')
plt.legend()
plt.show()

"""plt.plot(array_dynamique[2], array_dynamique[0], label='Optimized', color='orange')
plt.xlabel('nombre entrée')
plt.ylabel('temps execution (s)')
plt.legend()
plt.show()

plt.plot(array_dynamique[2], array_dynamique[1], label='Optimized', color='orange')
plt.ylim(0, 9)
plt.xlabel('nombre entrée')
plt.ylabel('Ram utilisée (Go)')
plt.legend()
plt.show()"""
