import random

def main():
    level = 1
    while True:
        try:
            x = int(input("Level: "))
            if x < level:
                continue
            else:
                level = x
                break
        except:
            pass
    number = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            else:
                guess = guess
            if guess == number:
                print("Just right!")
                break
            elif guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
        except:
            pass
if __name__ == "__main__":
    main()
