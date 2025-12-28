import random

def main():
    score = 0
    level = get_level()
    for _ in range(10):    
        x, y = generate_integer(level), generate_integer(level=level)

# --- LOOP THROUGH ATTEMPTS -- #
        attempt = 0
        while attempt < 3:
            try:
                answer = (int(input(f"{x} + {y} = ")))
                if answer != x + y:
                    print("EEE")
                    attempt += 1
                    if attempt == 3:
                        print(f"{x} + {y} = {x + y}")

                elif answer == x + y:
                    score += 1
                    break

            except ValueError:
                print("EEE")
                continue

    print(score)
        
# --- ASK USER FOR LEVEL --- #        
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

# --- GENERATE RANDOM INTEGERS FOR QUESTIONS --- #
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level == 2:
        x = random.randint(10, 99)
        return x
    elif level == 3:
        x = random.randint(100, 999)
        return x
    else:
        raise ValueError

if __name__ == "__main__":
    main()
    