def main():
    groceries = {}
    while True:
        try:
            item = input().lower()
            groceries[item] = groceries.get(item, 0) + 1
        except EOFError:
            for item in sorted(groceries):
                print(f"{groceries[item]} {item.upper()}")
            break

if __name__ == "__main__":
    main()