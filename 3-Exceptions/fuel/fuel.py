def main():
    while True:
        x = input("fuel: ")

        try:

            spl = x.split("/")

            i = int(spl[0])
            t = int(spl[1])

            if i > t or t == 0:
                continue

            q = round(i / t * 100)

            if q <= 1:
                print("E")
                break

            elif q >= 99:
                print("f")
                break

            print(f"{q}%")

            break

        except (ValueError, ZeroDivisionError):

            pass


main()
