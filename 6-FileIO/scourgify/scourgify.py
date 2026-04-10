import sys
import csv


script = len(sys.argv)

if script > 3:
    sys.exit("Too many command-line arguments")

elif script < 3:
    sys.exit("Too few command-line arguments")

argument = sys.argv[1]
newfile = sys.argv[2]

if not argument.endswith(".csv"):
    sys.exit(f"Could not read {argument}")

if not newfile.endswith(".csv"):
    sys.exit("Invalid File type(add .csv)")

try:
    with open(argument, newline="") as csvfile, open(
        newfile, "w", newline=""
    ) as outfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {argument}")
