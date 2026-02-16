name = input("Whats your name? ")

match name:
    case "Harry" | "piggy" | "eistein":
        print("Kingpig")
    case _:
        print("Who?")
