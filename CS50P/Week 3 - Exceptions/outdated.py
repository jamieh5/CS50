# Months dict with letter and numeric values
months = {
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

def main():
    while True:
        try:
            date = input("Date: ")
            valid = False
            month, day, year = "", "", ""
            if "/" in date:
                # Splitting the date into individual parts
                [month, day, year] = date.split("/")
                month = int(month)
            else:
                # Splitting the date into individual parts
                month_day, year = date.split(",")
                month, day = month_day.split(" ")

                # Converting month from letter to numeric
                for key in months:
                    if months[key][0][0:3] == month[0:3]:
                        month = key
                        break
            # Converting the individual parts into int´s
            day = int(day)
            year = int(year)
            # Checking if input is valid and either reprompting the user or printing the date in the desired format
            if (1 <= month <= 12) and day <= months[month][1] and year >= 0:
                valid = True
            else:
                valid = False
            if  valid == False:
                continue
            else:
                print(f"{year}-{month:02}-{day:02}")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()