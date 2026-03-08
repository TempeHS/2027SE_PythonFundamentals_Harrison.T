import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        break
    except ValueError:
        print("Please enter a valid number")

guess = random.randint(1, level)


while True:
    try:

        answer = int(input("Guess the number: "))

        if answer > guess:
            print("Too High!")
        elif answer < guess:
            print("Too Low!")
        else:
            print("Right on the money")
            break

    except ValueError:
        print("Enter a valid integer")
        break
