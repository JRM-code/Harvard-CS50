import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

font = figlet.getFonts()

# --- IF NO ARUGUMENTS INPUT, GIVE RANDOM FONT --- #
if len(sys.argv) == 1:
    font = random.choice(font)
    figlet.setFont(font=font)

# --- IF FONT ARGUMENT IS GIVEN --- #
elif len(sys.argv) == 3:
    if sys.argv[1] in ("-f", "--font"):
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid Usage")

else:
    sys.exit("Invalid Usage")

text = input("Enter text: ")

print(figlet.renderText(text))
