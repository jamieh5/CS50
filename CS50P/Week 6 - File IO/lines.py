# Problem set: https://cs50.harvard.edu/python/psets/6/lines/

import sys

def main():
    try:
        # Handling the incorrect command-line arguments
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif sys.argv[1].split(".")[len(sys.argv) - 1] != "py":
            sys.exit("Not a python file")

        # Opening the file
        with open(sys.argv[1]) as file:
            lines_count = 0

            # Counting how many lines of code are in the file, without comments and blank lines
            for line in file:
                if line.strip().startswith("#"):
                    continue
                elif line.strip() == "":
                    continue
                else:
                    lines_count += 1
            print(lines_count)

    except FileNotFoundError:
        sys.exit("File doesnt exit")
    except IndexError:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()