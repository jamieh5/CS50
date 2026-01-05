def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError

            fuel = x / y
            if fuel < 0 or fuel > 1:
                raise ValueError

            return round(fuel * 100)

        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


if __name__ == "__main__":
    main()
