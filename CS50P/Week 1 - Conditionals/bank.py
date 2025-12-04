def greeting(text):
    if text.startswith("hello"):
        return 0
    elif text.startswith("h"):
        return 20
    else:
        return 100

def main():
    output = greeting(input("Greeting: ").strip().lower())
    print(f"${output}")

if __name__ == "__main__":
    main()