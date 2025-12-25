# --- GET FRUIT FROM USER --- #
fruit_input = input("Input a fruit: ").lower()

# --- DICTIONARY OF FRUITS AND CALORIES --- #
fruits = {
    "apple": "130", "avocado": "50", "banana": "110",
    "cantaloupe": "50", "grapefruit": "60", "grapes": "90",
    "honeydew melon": "50", "kiwifruit": "90", "lemon": "15",
    "lime": "20", "nectarine": "60", "orange": "80", "peach": "60",
    "pear": "100", "pineapple": "50", "plums": "70", "strawberries": "50",
    "sweet cherries": "100", "tangerine": "50", "watermelon": "80", 
}

# --- TEST IF FRUIT IS IN DICT AND PRINT CALORIES --- #
if fruit_input in fruits:
    print(f"Calories: {fruits[fruit_input]}")
else:
    None
    