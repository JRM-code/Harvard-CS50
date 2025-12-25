# --- GET CAMEL STRING FROM THE USER --- #
camel = input("Write a camelCase string: ")

# --- LOOP OVER THE STRING, FIND UPPERS AND REPLACE --- #
for i in camel:
    if i.isupper():
        camel = camel.replace(i, '_' + i)

# --- CHANGE TO LOWER FOR SNAKE CASE --- #
snake = camel.lower()
print(snake)
