import sys
import csv
from tabulate import tabulate


def main():
    # Empty list to store contents of file
    pizza = []
    f_name = "sicilian.csv"
    # Checking for command line args
    if sys.argv[1] == f_name:
        # Opening a file in read mode
        with open("sicilian.csv") as file:
            # Setting the header
            header = ["Sicilian Pizza", "Small", "Large"]
            # Reading the contents of csv file
            read = csv.reader(file)
            for index, row in enumerate(read):
                # Storing in list
                if index == 0:
                    continue
                else:
                    pizza.append(row)
        print(tabulate(pizza, headers=header, tablefmt="grid"))


if __name__ == "__main__":
    main()
