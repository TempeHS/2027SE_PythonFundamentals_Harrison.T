def main():
    file = input().casefold()

    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".JPG"):
        print("image/jpeg")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".ZIP"):
        print("application/zip")
    elif file.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")


main()
