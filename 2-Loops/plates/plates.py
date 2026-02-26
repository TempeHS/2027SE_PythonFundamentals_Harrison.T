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

    if s[4:6].isnumeric():
        if s[6].isalpha():
            return False

    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True


main()
