def main():
    equation = input("Can you calculate: ")
    x, y, z = equation.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        print(x + z)
    elif y == "x":
        print(x * z)
    elif y == "-":
        print(x - z)
    elif y == "/":
        print(x / z)
    else:
        print("Invalid")


main()
