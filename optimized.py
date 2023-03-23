import pandas as pd

from utile import decorator, print_result

dataset1 = pd.read_csv('csv_file/dataset1.csv')
dataset2 = pd.read_csv('csv_file/dataset2.csv')
toto = ['price', 'profit']
print(dataset1.sort_values( 'profit'))
