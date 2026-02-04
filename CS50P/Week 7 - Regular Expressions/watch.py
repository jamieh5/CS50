import re

def main():
    print(parse(input("HTML: ")))

def parse(str):
    match = re.search(r'^<iframe .*src=".*youtube\.com/embed/([\w]+)".*></iframe>$', str)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()