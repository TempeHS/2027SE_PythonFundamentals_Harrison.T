names = {}

while True:
    try:
        item = input()

    except EOFError:

        for item in names:
            print(f"{names},and {item}")

        break
