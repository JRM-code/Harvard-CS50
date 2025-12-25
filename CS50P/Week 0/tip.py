# --- GET INPUT FROM THE USER AND CALCULATE TIP --- #
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# --- CONVERT THE DOLLAR AMOUNT TO A FLOAT --- #
def dollars_to_float(d):
    d = float(d.replace('$', ''))
    return d

# --- CONVERT THE TIP PERCENTAGE TO A FLOAT --- #
def percent_to_float(p):
    p = float(p.replace('%', ''))
    p = p / 100
    return p

main()