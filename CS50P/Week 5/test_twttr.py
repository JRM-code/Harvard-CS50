from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("TwitteR") == "TwttR"
    assert shorten("Twitter TeSt") == "Twttr TSt"
    assert shorten("twItter") == "twttr"
    assert shorten("123") == "123"
    assert shorten(".,?") == ".,?"
    assert shorten("CS50") == "CS50"

if __name__ == '__main__':
    main()