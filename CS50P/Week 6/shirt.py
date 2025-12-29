import sys
import csv
import os
from PIL import Image, ImageOps

arg1_split = os.path.splitext(sys.argv[1])
arg2_split = os.path.splitext(sys.argv[2])
arg1_ext, arg2_ext = arg1_split[1].lower(), arg2_split[1].lower()

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not arg1_ext in [".jpg", ".jpeg", ".png"]:
    print("Not an image file")
    sys.exit(1)
elif not arg2_ext in [".jpg", ".jpeg", ".png"]:
    print("Your new file should be an image file")
    sys.exit(1)
elif arg1_ext != arg2_ext:
    sys.exit(1)
else:
    pass

shirt = Image.open("shirt.png")
shirt_size = shirt.size

before = Image.open(sys.argv[1])

muppet = ImageOps.fit(before, size=shirt_size) 
muppet.paste(shirt, shirt)
muppet.save(sys.argv[2])
