# --- GET USER INPUT AND CALL CALC FUNCTION --- #
def main():
    fuel = fuel_calc("Fraction: ")

# --- CHECK FUEL LEVEL AND PRINT --- #
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def fuel_calc(prompt):
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split('/')
            percent = round(int(numerator)/int(denominator)*100)
            if percent >= 0 and percent <= 100:
                return percent

        except (ValueError, ZeroDivisionError):
            pass

main()