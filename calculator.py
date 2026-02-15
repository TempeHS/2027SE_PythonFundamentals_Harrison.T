def hello(to="world"):
    # defines hello, with anything under the colon. "Makes to = world as default value"
    print("hello,", to)


hello()
name = input("Whats your name? ")
hello(name)
# Name is being converted into "To" which in the def command the "to" is the "name"


## x = float(input("What's X? "))     Like an int but more specific, adds decimal points or whatnot
## y = float(input("What's Y? "))


## z = round(x / y, 2)  # round to 2 digits
# z = x / y

# print(z)

## print(f"{z:.2f}")
# - If you forget the round, and want to round it by using an f string 2f is how many digits you want to print
