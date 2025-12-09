owed = 50
while owed > 0:
    print(f"Amount due: {owed}")
    paid = int(input("Insert coin: "))

    if paid == 5 or paid == 10 or paid == 25:
        owed = owed - paid
    else:
        print(f"Amout due: {owed}")

if owed == 0:
    print("Change owed: 0")
else:
    print(f"Change owed: {abs(owed)}")