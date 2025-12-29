import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("Not a .csv file")
    sys.exit(1)
elif not sys.argv[2].endswith(".csv"):
    print("Your new file should end with .csv")
    sys.exit(1)
else:
    pass

new_file = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]
            new_file.append({"first": first, "last": last, "house": house})

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)


with open(sys.argv[2], "w") as write_file:
    writer = csv.DictWriter(write_file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in new_file:
        writer.writerow(row)
