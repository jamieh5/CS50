from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    text = ""

    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=random.choice(fonts))
    elif sys.argv[1] == "-f" and sys.argv[2] in fonts and len(sys.argv) == 3:
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
    else:
        print("Invalid Usage")
        sys.exit(1)
    output = figlet.renderText(text)
    print(output)

if __name__ == "__main__":
    main()
