def main():
    time = input("What's the time? ")
    convert(time)


def convert(t):
    t = t.replace(":", "")
    t = int(t)

    if 800 >= t >= 700:
        print("Breakfast")
    elif 1300 >= t >= 1200:
        print("Lunch time")
    elif 1900 >= t >= 1800:
        print("Dinner time")
    else:
        print("No food")


if __name__ == "__main__":
    main()
