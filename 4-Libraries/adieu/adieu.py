names = []

while True:
    try:
        item = input().title()

        if item.isalpha():
            names.append(item)

    except EOFError:
        if len(names) == 1:
            print(f"Adieu, adieu, to {names[0]}")
        elif len(names) == 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}")
        elif len(names) > 2:
            print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")
        break
