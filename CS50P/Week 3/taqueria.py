# --- DICTIONARY OF ENTREES --- #
entrees = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# --- INITIALISE TOTAL VARIABLE --- #
total = 0

# --- GET INPUT AND ADD TOTAL UNTIL DONE --- #
while True:
    try:
        item = input("Item: ").title()  
        if item in entrees:
            total += entrees[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        break
            


