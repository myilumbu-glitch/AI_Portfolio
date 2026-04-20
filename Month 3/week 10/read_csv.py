#CSV Lecture Notes (09.04.26)

import csv

scores = []


with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader) #skips header row

    for row in reader:
          score = int(row[2])
          scores.append(score)

print("All scores:", (scores))
