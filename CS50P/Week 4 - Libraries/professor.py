import random

def main():
    score = 0
    equations = 0
    level = get_level()
    while equations < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        guesses = 0
        while True:
            try:
                equation = int(input(f"{x} + {y} = "))
                if equation == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    guesses += 1
                    if guesses == 3:
                        print(x + y)
                        break
            except:
                pass
        equations += 1
    print(score)

def get_level():
    level = 0
    while True:
        try:
            x = int(input("Level: "))
            if 1 <= x <= 3:
                level = x
                break
            else:
                continue
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
       return random.randint(10, 99)
    elif level == 3:
       return random.randint(100, 999)

if __name__ == "__main__":
    main()