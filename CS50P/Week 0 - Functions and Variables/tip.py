def dollars_to_float(text):
    money = text.replace("$", "")
    return float(money)

def percent_to_float(text):
    percent = text.replace("%", "")
    return float(percent)

def main():
    mealCost = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = mealCost * (percent / 100)
    print("Leave $" + format(tip, ".2f"))

if __name__ == "__main__":
    main()
