def main():
    x = input("Input: ")

    i = x[0:1]
    t = x[1:2]
    g = x[2:3]

    if not t == "/":
        print("Invalid")
        return False

    if len(x) != 3:
        print("Invalid")
        return False

    print(x)


main()
