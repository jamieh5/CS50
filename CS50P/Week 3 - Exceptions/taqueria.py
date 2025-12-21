def main():
    entrees = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total_price = 0
    while True:
        try:
            item = input("Item: ").title()
            total_price += entrees[item]
            print(f"Total: ${"%.2f" % total_price}")
        except EOFError:
            break
        except KeyError:
            pass

if __name__ == "__main__":
    main()
