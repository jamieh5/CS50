def main():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                num_of_hashtags = 1
                num_of_spaces = int(height) - 1

                for i in range(0, height, 1):
                    print(" " * num_of_spaces + "#" * num_of_hashtags + "  " + "#" * num_of_hashtags)
                    num_of_hashtags += 1
                    num_of_spaces -= 1
                break
        except ValueError:
            print("Enter a number between 1 and 8")
if __name__ == "__main__":
    main()
