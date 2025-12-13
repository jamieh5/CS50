def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            fuel = int(x) / int(y)
            if fuel < 0 or fuel > 1:
                continue
            elif 0.99 <= fuel:
                print("F")
                break
            elif 0 <= fuel <= 0.01 :
                print("E")
                break
            else:
                print(f"{round(fuel * 100)}%")
                break
        except (ValueError, ZeroDivisionError):
            x, y = input("Fraction: ").split("/")


if __name__ == "__main__":
    main()