def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    for i, dd in enumerate(s):
        if dd.isdigit():
            if dd == "0":
                return False
            if not s[i:].isdigit():
                return False

            break

    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
