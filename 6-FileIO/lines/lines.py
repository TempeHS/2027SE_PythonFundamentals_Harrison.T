import sys


num_arguments = len(sys.argv)


if num_arguments < 2:
    sys.exit("Too Many Arguments")

elif num_arguments > 2:
    sys.exit("Too Few Arguments")


filename = sys.argv[1]


if not filename.endswith(".py"):
    sys.exit("Not a python script")


try:
    with open(filename) as file:
        counter = 0
        for line in file:
            amountline = line.lstrip()
            if not amountline:
                continue
            if amountline.startswith("#"):
                continue
            counter += 1

        print(f"Number of lines {counter}")

except FileNotFoundError:
    sys.exit("File Does Not Exist!")
