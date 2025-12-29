import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".py"):
    print("Not a python file")
    sys.exit(1)
else:
    pass

count = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            count += 1
            if line.lstrip().startswith("#"):
                count -= 1
            elif line.split() == []:
                count -= 1

except FileNotFoundError:
    print("File does not exist")
    sys.exit()

print(count)