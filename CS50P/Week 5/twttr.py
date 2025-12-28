def main():
    word = shorten(input("Enter a word: "))
    print(word)

def shorten(word):
    for i in word:
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            word = word.replace(i, '')
    return word

if __name__ == "__main__":
    main()
