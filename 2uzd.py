import csv
with open("2.uzd.csv", encoding="utf-8") as fg:
    data = csv.DictReader(fg)
    for kolona in data:
        print(kolona['uzvārds'])

