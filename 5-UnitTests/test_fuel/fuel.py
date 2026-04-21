def main():
    fuel = input("What's your fuel at? ")
    print(convert(fuel))


def convert(fraction):
    while True:
        try:

            x = fraction[0:1]
            z = fraction[2 : len(fraction)]
            x = int(x)
            z = int(z)
            percentage = x / z * 100
            break
        except (ValueError, ZeroDivisionError):
            pass
    if percentage >= 100:
        return "F"
    elif percentage == 0:
        return "E"
    else:
        percentage = str(percentage)
        percentage = percentage.partition(".")[0]
        percentage += "%"
        return percentage


if __name__ == "__main__":
    main()
