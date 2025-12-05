def main():
    time = input("What time is it? ")
    print(mealTime(convert(time)))

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    time = int(hours) + minutes
    return time

def mealTime(time):
    if time >= 7.00 and time <= 8.00:
        return "breakfast time"
    elif time >= 12.00 and time <= 13.00:
        return "lunch time"
    elif time >= 18.00 and time <= 19.00:
        return "dinner time"

if __name__ == "__main__":
    main()
