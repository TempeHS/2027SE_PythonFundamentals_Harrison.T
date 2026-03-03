import emoji

transfer = input("Input emoji alias: ")
transformed = emoji.emojize(transfer)
print(transformed)
