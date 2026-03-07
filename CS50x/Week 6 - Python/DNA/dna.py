import csv
import sys


def main():
    # Checking for correct command-line input
    if len(sys.argv) != 3:
        print("Wrong command-line input")
    
    # Defining a function to read the file and saving in the variables
    def load_files(filename):
        with open(filename) as file:
            return file.read().strip()

    dna = load_files(sys.argv[1])
    database = load_files(sys.argv[2])
    
    # Getting the counts for the consecutive runs of each STR in the DNA sequence and saving in a dictionary
    sequences = ["AGAT", "AATG", "TATC"]
    count_dict = {}
    for seq in sequences:
        count_dict[seq] = longest_match(dna, seq)

    # TODO: Check database for matching profiles

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
