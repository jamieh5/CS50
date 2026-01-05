from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Twitter") == "Twttr", print("Twitter doesnt equal Twttr")
    assert shorten("What's your name?") == "Wht's yr nm?", print("What's your name? doesnt equal Wht's yr nm?")
    assert shorten("CS50") == "CS50", print("CS50 doesnt equal CS50")
    assert shorten("TWITTER") == "TWTTR", print("TWITTER doesnt equal TWTTR")

if __name__ == "__main__":
    main()
