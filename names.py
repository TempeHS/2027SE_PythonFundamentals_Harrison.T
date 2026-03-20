names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")


##with open("names.", "r") as file:
# for line in file:
# print("hello", line.rstrip())


## name = input("Whats your name? ")

# with open("names.txt", "a") as file:  ## a for append   w for write
#   file.write(f"{name}\n")


## names = []

# for _ in range(3):
#    names.append(input("What's your name? "))

# for name in sorted(names):
#    print(f"hello, {name}")
