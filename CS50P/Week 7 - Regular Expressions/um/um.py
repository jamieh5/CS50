# Problem set: https://cs50.harvard.edu/python/psets/7/um/

import re


def main():
    print(count(input("Text: ")))


def count(str):
    matches = re.findall(r"\bum\b", str, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
