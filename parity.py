def main():
    x = int(input("Whats x? "))
    if is_even(x):
        print("even")
    else:
        print("ood")


def is_even(n):
    return True if n % 2 == 0 else False


main()
