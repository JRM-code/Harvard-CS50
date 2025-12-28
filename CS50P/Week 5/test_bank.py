from bank import value

def main():
    test_bank()
    test_upper()

def test_bank():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("whats up") == 100

def test_upper():
    assert value("HELLO") == 0

if __name__ == '__main__':
    main()