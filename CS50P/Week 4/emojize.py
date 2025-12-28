import emoji

string = input("Enter an emoji string: ")

print(emoji.emojize(f"{string}", language='alias'))