from um import count

def main():
    test_um()
    test_yum()
    test_zero()

def test_um():
    assert count("um") == 1
    assert count("um, um, um") == 3
    assert count("Um, thanks for the album.") == 1

def test_yum():
    assert count("um, yum, um") == 2
    assert count("yummy") == 0

def test_zero():
    assert count("CS50") == 0
    assert count("Thanks for the album.") == 0

if __name__ == '__main__':
    main()