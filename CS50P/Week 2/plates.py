# --- GET PLATE FROM USER --- #
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# --- CHECK IF PLATE IS VALID --- #
def is_valid(plate):
    if plate.isalpha() and len(plate) >= 2 and len(plate) <= 6:
        return True
    elif plate[0:2].isalpha():
        for i in plate:
            if i.isdigit():
                dig_pos = plate.index(i)
                if plate[dig_pos:].isdigit() and i != "0":
                    return True
                else:
                    return False
main()

