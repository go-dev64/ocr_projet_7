import csv
from bruteforce_iteration import bin_function
from decorateur import loop
from bruteforce_recursive import start

with open('csv_file/dataset_20.csv', newline='') as f:
    reader = csv.reader(f)
    header = [next(reader)]
    list_action_dataset_20 = [[row[0], int(row[1]), int(row[2])] for row in reader]

data_time = []

def main():
    loop(list_action_dataset_20, bin_function)
    loop(list_action_dataset_20, start)

if __name__ == "__main__":
    main()