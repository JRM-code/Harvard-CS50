from numb3rs import validate

def main():
    test_structure()
    test_nums()

def test_structure():
    assert validate("1.1.1.1") == True
    assert validate("10.10.10.10") == True
    assert validate("100.100.100.100") == True
    assert validate("1.1.1.") == False
    assert validate("10.10") == False
    assert validate("100") == False

def test_nums():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.1.1.1") == False
    assert validate("001.255.255.255") == False
    assert validate("1.256.1.1") == False

if __name__ == '__main__':
    main()
