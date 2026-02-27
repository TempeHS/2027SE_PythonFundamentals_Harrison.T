def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    return float(d.replace("$", "").replace(",", "").strip())
    ##Removes dollar signs and commas, strips whitespace, then converts to float.
    ##Example: "$1,234.50" -> 1234.5.


def percent_to_float(p):

    return float(p.replace("%", "").strip()) / 100
    ##Removes percent sign, strips whitespace, converts to float, then divides by 100.
    ##Example: "15%" -> 0.1


main()
