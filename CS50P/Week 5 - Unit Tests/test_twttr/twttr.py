def shorten(text):
    vowels = ["A", "E", "I", "O", "U"]
    output = ""
    for c in text:
        if c.upper() not in vowels:
            output += c
    return output


def main():
    text = input("Input: ")
    print(shorten(text))

if __name__ == "__main__":
    main()
