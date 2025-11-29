def dollars_to_float(meal_cost):
    return meal_cost

meal_cost = dollars_to_float(meal_cost = input("How much was your meal? "))

drop_dol = float(meal_cost.replace('$', ''))

print(drop_dol)