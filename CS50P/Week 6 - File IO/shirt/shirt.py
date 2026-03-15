# Problem-set: https://cs50.harvard.edu/python/psets/6/shirt/
import sys
import os
from PIL import Image, ImageOps

def main():
    input_validating()

def input_validating():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    endings = [".jpeg", ".jpg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])[1]
    ext2 = os.path.splitext(sys.argv[2])[1]
    if ext1 != ext2 or ext1 not in endings:
        sys.exit("Invalid input")


def overlap_images():
    try:
        before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input doesnt exist")
    before = ImageOps.fit(before, shirt.size)
    before.paste(shirt, shirt)
    before.save(sys.argv[2])


if __name__ == "__main__":
    main()
