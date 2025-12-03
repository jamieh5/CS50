def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return(text)

def main():
    sentence = input("Enter a sentence with a smiley face: ")
    print(convert(sentence))

if __name__ == "__main__":
    main()
