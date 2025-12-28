from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_errors()

# --- TEST CONVERSIONS TO PERCENTAGES --- #
def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100

# --- TEST GAUGE READINGS --- #
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

def test_errors():
    with pytest.raises(ValueError):
        convert("foo/bar")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

if __name__=='__main__':
    main()
