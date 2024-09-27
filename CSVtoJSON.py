import csv
import json

VERSION_STRING = "0.0.1"


def convert(direction, csv_header, from_file, to_file):
    data = []

    if direction == 1 and csv_header == 1:
        with open(from_file, mode="r", newline="") as csvread:
            csvreader = csv.reader(csvread)
            headings = next(csvreader)
            for row in csvreader:
                convertedRow = {}
                i = 0
                while i < len(headings):
                    convertedRow[headings[i]] = row[i]
                    i += 1
                data.append(convertedRow)

        with open(to_file, mode="w", encoding="utf-8") as jsonwrite:
            json.dump(data, jsonwrite, indent=4)
            jsonwrite.write

    if direction == 1 and csv_header == 0:
        with open(from_file, mode="r", newline="") as csvread:
            csvreader = csv.reader(csvread)
            for row in csvreader:
                convertedRow = {}
                i = 0
                while i < len(row):
                    convertedRow[i] = row[i]
                    i += 1
                data.append(convertedRow)

        with open(to_file, mode="w", encoding="utf-8") as jsonwrite:
            json.dump(data, jsonwrite, indent=4)
            jsonwrite.write

    if direction == 2:
        with open(from_file, mode="r") as jsonread:
            data = json.load(jsonread)

        with open(to_file, mode="w", newline="") as csvwrite:
            row = csv.writer(csvwrite)
            for line in data:
                convertedRow = []
                for x in line.values():
                    convertedRow.append(x)
                row.writerow(convertedRow)

    else:
        print("Handle this issue")


def main():
    direction = 1  # 1 - CSV to JSON, 2 - JSON to CSV
    csv_header = 0  # 0 - No header, 1 - Header
    from_file = ""
    to_file = ""

    print(f"Welcome to CSVtoJSON version {VERSION_STRING}")
    print("Please select the direction you would like to work.")
    print("Enter 1 for CSV to JSON or 2 for JSON to CSV")
    direction = int(input("Direction (1 or 2): "))

    if direction == 1:
        print("Please enter the file to convert. (ex. convertMe.csv)")
        from_file = input("File to convert: ")
        print("Does your .csv file have a header row?")
        csv_header = int(input("0 = No, 1 = Yes: "))
        print("Please enter a name for your new JSON file. (ex. convertedFile.json)")
        to_file = input("Filename: ")
    elif direction == 2:
        print("Please enter the file to convert. (ex. convertMe.json)")
        from_file = input("File to convert: ")
        print("Please enter a name for your new .csv file. (ex. convertedFile.csv)")
        to_file = input("Filename: ")

    print("Converting...")
    convert(direction, csv_header, from_file, to_file)
    print("Done!")


main()
