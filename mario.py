def main():
    print_sqaure(3)


def print_sqaure(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()


##def main():
# print_column(3)


##def print_column(height):
#  print("#\n" * height, end="")


##main()
