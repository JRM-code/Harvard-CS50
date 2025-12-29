import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("Not a csv file")
    sys.exit(1)
else:
    pass

table = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)