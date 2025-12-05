def main():
    camel_case = input("camelCase: ").strip()
    print(convert(camel_case))

def convert(text):
    snake_case = ""
    for char in text:
        if char.islower():
            snake_case += char
        else:
            snake_case = snake_case + "_" + char.lower()
    return snake_case

if __name__ == "__main__":
    main()