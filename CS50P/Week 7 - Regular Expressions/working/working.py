# Problem set: https://cs50.harvard.edu/python/psets/7/working/
# Converting the time while only being allowed to use the re and sys library

def main():
    print(convert(input("Hours: ")))

# 9:00 AM to 5:00 PM

def convert(text):
    # Splitting the string
    try:
        first, second = text.split(" to ")
        first = first.split(" ")
        second = second.split(" ")
        first = check(first[0], first[1])
        second = check(second[0], second[1])
        return f"{first} to {second}"
    except:
        raise ValueError

def check(str, period):
    time = str.split(":")

    # If the time string doesnt contain a value for the minutes -> 0 gets added to the time arr
    if len(time) == 1:
        time.append("00")

    # Creating the hour and minute variables and converting them to int
    hour, minute = time
    if len(minute) != 2:
        raise ValueError
    
    hour = int(hour)
    minute = int(minute)

    # Checking if the values are valid and raising a ValueError if not
    if hour == 12 and period.lower() == "am":
        hour -= 12
    elif hour == 12 and period.lower() == "pm":
        hour = 12
    elif not (0 <= hour <= 11 and 0 <= minute <= 59):
        raise ValueError

    if period.lower() == "pm" and hour != 12:
        hour += 12
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
