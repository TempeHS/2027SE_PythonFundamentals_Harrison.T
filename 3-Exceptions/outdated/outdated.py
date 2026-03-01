def main():

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                spl = date.split("/")

                i = int(spl[0])
                t = int(spl[1])
                g = int(spl[2])

                for number in months:
                    if i == months[number]:
                        i = i

                        if t <= 31 or t > 0:

                            print(f"{g:04}-{i:02}-{t:02}")
                            return

            elif "," in date:
                spl = date.split(",")

                left = spl[0].strip().split()

                j = left[0]
                k = left[1]

                right = spl[1]

                if j in months:
                    j = months[j]
                    k = int(k)
                    right = int(right)

                    if k <= 31 or k > 0:

                        print(f"{right:04}-{j:02}-{k:02}")

                        break

        except ValueError:
            print("Invalid input")
            pass

        except EOFError:
            print()
            break


months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


main()
