camel = input("What is your variable name? ")
possum = ""

for character in camel:
    if character.isupper():
        possum += "_" + character.lower()
    else:
        possum += character

print(possum)
