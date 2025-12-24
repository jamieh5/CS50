def main():
    coins = 0
    def convert(change, coin, coins):
        coins += int(change / coin)
        change = change % coin
        return coins, change
    while True:
        try:
            change = input("Change: ")
            if float(change) < 0.00:
                continue
            change = round(float(change) * 100)
            [coins, change] = convert(change, 25, coins)
            [coins, change] = convert(change, 10, coins)
            [coins, change] = convert(change, 5, coins)
            [coins, change] = convert(change, 1, coins)
            print(coins)
            break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
