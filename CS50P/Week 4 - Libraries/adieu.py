def main():
    names = []
    text = "Adieu, adieu, "
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break
    text += f"to {names[0]}"
    counter = 1
    while counter < len(names):
        if len(names) == 2:
            text += f" and {names[counter]}"
        else:
            if counter == len(names) - 1:
                text += f", and {names[counter]}"
            else:
                text += f", {names[counter]}"
        counter += 1

    print(f"\n{text}")

if __name__ == "__main__":
    main()
