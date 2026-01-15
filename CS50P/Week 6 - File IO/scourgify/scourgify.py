import csv
import sys

def main():
    # Handling command-line arguments
    if len(sys.argv) > 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")

    input_data = []
    # Reading the input data and appending it
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for line in reader:
            input_data.append(line)

    # Changing the data into the correct format and writing the new file
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "house"])
        for line in input_data[1:]:
            last, first = line[0].split(",")
            writer.writerow([first.strip(), last.strip(), line[1]])

if __name__ == "__main__":
    main()
