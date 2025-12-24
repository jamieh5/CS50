def main():
    letters = 0
    words = 1
    sentences = 0
    text = input("Text: ")
    for char in text:
        char = ord(char)
        if char == 32:
            words += 1
        elif char == 33 or char == 46 or char == 63:
            sentences += 1
        elif char > 64 and char < 91:
            letters += 1
        elif char > 96 and char < 123:
            letters += 1
    l = float(letters / words * 100)
    s = float(sentences / words * 100)

    grade = round(0.0588 * l - 0.296 * s - 15.8)

    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")

if __name__ == "__main__":
    main()
