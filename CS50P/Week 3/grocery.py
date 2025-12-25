# --- CREATE AN EMPTY DICTIONARY --- #
groceries = {}

# --- GET ITEMS FROM USER --- #
while True:
    try:
        item = input().upper()
    except EOFError:
            break

# --- ADD THE ITEM TO THE DICTIONARY OR UPDATE VALUE --- #
    if item not in groceries:
        groceries[item] = 1
    else:
         groceries[item] += 1

groceries.update(groceries)

# --- SORT DICTIONARY ALPHABETICALLY AND PRINT --- #
sorted_dict = dict(sorted(groceries.items()))

for key, value in sorted_dict.items():
    print(f"{value} {key}")

