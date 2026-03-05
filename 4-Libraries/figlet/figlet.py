from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    pass


elif len(sys.argv) == 3:
    s = sys.argv[1]
    f = sys.argv[2]

    if s != "-f" and s != "--font":
        sys.exit("InVALID")


else:
    sys.exit("Invalid arguments")

figlet.setFont(font=f)

text = input("Input: ")

print(figlet.renderText(text))
