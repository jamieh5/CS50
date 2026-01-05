def is_valid(text):

    if not (2 <= len(text) <= 6):
        return False

    if not (text[0].isalpha() and text[1].isalpha()):
        return False

    if not text.isalnum():
        return False

    number_started = False
    for c in text:
        if c.isdigit():
            if not number_started:
                if c == '0':
                    return False
                number_started = True
        else:
            if number_started:
                return False

    return True

def main():
    text = input("Plate: ")
    if is_valid(text):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
