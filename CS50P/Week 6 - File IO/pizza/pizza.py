import sys
from tabulate import tabulate
import csv

def main():
    try:
        # Handling command line arguments
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        file_name = sys.argv[1].split(".")
        if file_name[len(file_name) - 1] != "csv":
            sys.exit("Not a csv file")

        # Opening the file
        with open(sys.argv[1]) as file:
            data = []
            reader = csv.reader(file)
            # print(tabulate(table, headers, tablefmt="pretty"))
            for row in reader:
                data.append(row)
            print(tabulate(data[1:], data[0], tablefmt="grid"))
    # Exits the programm if input file in argv[1] doesnt exit
    except FileNotFoundError:
        sys.exit("File does not exit")

if __name__ == "__main__":
    main()
