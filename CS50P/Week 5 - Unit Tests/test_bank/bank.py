def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    output = value(input("Greeting: ").strip().lower())
    print(f"${output}")

if __name__ == "__main__":
    main()
