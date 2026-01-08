from working import convert
import pytest

def main():
    test_format()
    test_range()
    test_hours()

def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_range():
    with pytest.raises(ValueError):
        convert("9 to 5 ") 
    with pytest.raises(ValueError):     
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):     
        convert("9AM to 5PM")
    with pytest.raises(ValueError):     
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):     
        convert("09:00 AM 5:00 PM")


def test_hours():
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
    assert convert("12:00 AM to 5:00 PM") == "00:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

if __name__ == '__main__':
    main()
    