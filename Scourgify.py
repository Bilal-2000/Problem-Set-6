import sys
import csv


def main():
    store = []
    # Checking for len of sys arg
    if len(sys.argv) == 3:
        if sys.argv[1] == "before.csv":
            # Storing filename in a var
            f_name = sys.argv[2]
            # Opening already present file
            with open("before.csv") as file:
                for index, row in enumerate(file):
                    # IF first iteration unpack list using 2 var only
                    if index == 0:
                        first_n, house = row.split(",")
                        store.append(
                            [first_n, "second_name", house.strip()])
                    else:
                        # Unpack list in 3 vars
                        first_n, second_n, house = row.split(",")
                        # Appending the values in list with striping off whitespaces and ""
                        store.append(
                            [first_n.strip("\"").lstrip(), second_n.strip("\"").lstrip(), house.strip().lstrip()])

            # Open a new file to write and ignoring new line
            with open(f_name, "w", newline='') as new:
                # Storing return value of writer in a var
                writer = csv.writer(new)
                for row in store:
                    # Writing a row in file
                    writer.writerow(row)


if __name__ == "__main__":
    main()
