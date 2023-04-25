import numpy as np

import matplotlib.pyplot as plt

from bruteforce import list_action_dataset_20, recursivity, iteration

from optimized import dynamique, data1, data2, data20

from utile import loop


array_recursive = loop(list_action_dataset_20, recursivity, 25)
print(array_recursive[0])
array_binary = loop(list_action_dataset_20, iteration, 25)
print(array_binary[0])

array_dynamique = loop(data1, dynamique, 1000)


plt.plot(array_recursive[2], array_recursive[0], label='bruteForce récursif', color='blue')
plt.plot(array_binary[2], array_binary[0], label='bruteForce itératif', color='green')
plt.xlabel('nombre entrée')
plt.xlim(0, len(array_binary[2]) + 1)
plt.ylabel('temps execution (s)')
plt.legend()
plt.show()

plt.plot(array_recursive[2], array_recursive[1], label='bruteForce récursif', color='blue')
plt.plot(array_binary[2], array_binary[1], label='bruteForce itératif', color='green')
plt.xlim( 0, len(array_binary[2]) + 1)
plt.xlabel('nombre entrée')
plt.ylabel('Ram utilisée (Go)')
plt.legend()
plt.show()
