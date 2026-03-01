def main():

    total = 0.00

    while True:
        try:
            item = input("What are you buying? ").title()

            for food in menu:
                if food == item:
                    total = total + menu[food]
                    print("Good choice")

        except EOFError:
            print()
            print(f"Your total is: ${total:.2f}")
            break


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


main()
