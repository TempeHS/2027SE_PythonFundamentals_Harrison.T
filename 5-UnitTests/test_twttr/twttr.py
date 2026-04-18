def main():
    twitter = input("Say something: ").casefold
    print(shorten(twitter))


def shorten(word):
    result = ""
    not_allowed = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter not in not_allowed:
            result += letter
    return result


if __name__ == "__main__":
    main()
