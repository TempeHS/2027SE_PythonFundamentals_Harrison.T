from datetime import date
import sys
import inflect


p = inflect.engine()


def main():
    bdate = ask_date()
    today = current_date()
    ddays = today - bdate
    minuts = ddays.days * 24 * 60
    print(word_time(minuts))


def ask_date():
    bdate = input("Date: YYYY-MM-DD ")
    try:
        year, month, day = bdate.split("-")
    except ValueError:
        sys.exit("Input the date to the correct syntax")
    try:
        month = int(month)
        day = int(day)
    except ValueError:
        sys.exit("Input Numbers")
    if month > 12:
        sys.exit("Month numbers do not go above twelve")
    elif day > 31:
        sys.exit("Days do not go above 31")
    bdate = date.fromisoformat(bdate)
    return bdate


def current_date():
    currentDate = date.today()
    return currentDate


def word_time(minutes):
    words = p.number_to_words(minutes, andword=",")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
