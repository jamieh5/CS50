# Problem set: https://cs50.harvard.edu/python/psets/8/seasons/

from datetime import date
from sys import exit

import inflect

def main():
    birth_date = input("Date of birth: ")
    valid_date(birth_date)
    convert(birth_date)

def valid_date(birth_date):
    try:
        date.fromisoformat(birth_date)
    except ValueError:
        exit("Invalid date")

def convert(birth_date):
    today = date.today()
    birth_date = date.fromisoformat(birth_date)
    difference = today - birth_date
    total_minutes = int(difference.total_seconds() / 60)
    total_minutes = inflect.engine().number_to_words(total_minutes, andword="").capitalize()
    print(f"{total_minutes} minutes")

if __name__ == "__main__":
    main()
