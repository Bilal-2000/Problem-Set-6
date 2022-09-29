import sys


def main():
    # Def the name of file
    f_name = "loc.py"
    count = 0

    # To check if the arg is provided or not
    try:
        # Checking the name of file
        if sys.argv[1] == f_name:
            # Opening a file in read mode
            with open(f_name) as file:
                # Iterating over line in file
                for line in file:
                    # If Comment or White space present ignore
                    if line.startswith("#") or line.isspace():
                        continue
                    else:
                        count += 1
            # Printing the no of lines
            print(count)

        elif sys.argv[1] != f_name:
            # Unpacking of list
            first, second = sys.argv[1].split(".")
            # Checking the extension of file
            if second != "py":
                print("Not a python file")
            # If file doesn't exist
            else:
                print("File does not exist")

        # Too much argument given
        elif len(sys.argv) > 1:
            print("Too many argument provided")

    except (IndexError, ValueError):
        print("Too few command-line arguments")
        sys.exit()


if __name__ == "__main__":
    main()
