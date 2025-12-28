from plates import is_valid

def main():
    test_length()
    test_nums()
    test_order()
    test_zero()
    test_specs()

# --- TEST LENGTH (2 - 6) --- #
def test_length():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") == False 

# --- FIRST TWO CHARS ARE LETTERS --- #
def test_nums():
    assert is_valid("12") == False
    assert is_valid("AA123") == True
    assert is_valid("AAA123") == True
    assert is_valid("12AAA") == False
    assert is_valid("123AAA") == False

# --- NO LETTERS AFTER NUMBERS --- #
def test_order():
    assert is_valid("AA12A") == False
    assert is_valid("AA1AA") == False
    
# --- FIRST NUMBER IS NOT 0 --- #
def test_zero():
    assert is_valid("AA012") == False

# --- NO SPECIAL CHARS --- #
def test_specs():
    assert is_valid("AA.A12") == False
    assert is_valid("AA,12") == False
    assert is_valid("AA1!3") == False

if __name__ == '__main__':
    main()