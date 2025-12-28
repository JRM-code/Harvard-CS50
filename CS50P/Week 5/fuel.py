def main():
    trys = True
    while trys:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            fuel = gauge(percentage)
            trys = False
            print(fuel)
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    numerator, denominator = fraction.split('/')
    percentage = round(int(numerator)/int(denominator)*100)
    if percentage >= 0 and percentage <= 100:
        return percentage
    
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()
