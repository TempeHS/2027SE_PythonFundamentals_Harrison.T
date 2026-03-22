import sys


num_arguments = len(sys.argv)


if num_arguments == 2:
    first_arg = sys.argv[1]
    print(f"Number of arguments: {num_arguments}")

if num_arguments > 2:
    print("Too many arguments")
    sys.exit

if num_arguments < 1:
    print("Too Few Arguments")
    sys.exit

try:
    with open("first_arg", "r") as file:
        content = file.read()
        for line in file:
            first_arg.append(line.rstrip())

        print()

except FileNotFoundError:
    sys.exit
