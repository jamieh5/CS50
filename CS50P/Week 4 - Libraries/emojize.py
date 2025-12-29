import emoji

def main():
    text = emoji.emojize(input("Input: "), language="alias")
    print(f"Output: {text}")

if __name__ == "__main__":
    main()