from tabulate import tabulate
import sys
import csv

pizza = len(sys.argv)


if pizza > 2:
    sys.exit("Too Many Arguments")

elif pizza < 2:
    sys.exit("Too Few Arguments")


menu = sys.argv[1]


if not menu.endswith(".csv"):
    sys.exit("Not a validated menu")

try:
    with open(menu) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))


except FileNotFoundError:
    sys.exit("File Does Not Exist!")
