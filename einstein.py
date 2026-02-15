def main():
    n = int(input("Mass: "))
    print("Equivalent : ", Equivale(n))


def Equivale(n):
    e = 300000000
    return n * e * e


main()
