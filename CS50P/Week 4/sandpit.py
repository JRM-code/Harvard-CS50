import random

score = 0
attempt = 0

for i in range(10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = (int(input(f"{x} + {y} = ")))
    if answer == x + y:
        score += 1
    else: 
        attempt += 1
        if attempt == 3:
            print(f"{x} + {y} = {x + y}")
print(score)