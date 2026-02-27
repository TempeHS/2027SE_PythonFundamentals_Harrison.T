n = input("Enter the number 42: ")

match n:
    case "42" | "Forty Two" | "forty-two":
        print("Yes thats 42")
    case _:
        print("No thats not 42 try again. ")
