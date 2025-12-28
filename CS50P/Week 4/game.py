import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            level = random.randrange(0, level, 1)
            break

    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < level:
                print("Too small!")
                continue
            elif guess > level:
                print("Too large!")
                continue
            elif guess == level:
                print("Just right!")
                break
    except ValueError:
        continue