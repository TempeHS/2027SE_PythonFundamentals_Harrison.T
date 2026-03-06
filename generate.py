import random

# coin = random.choice([heads, tails])

# number = random.randint(1,100)


cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
