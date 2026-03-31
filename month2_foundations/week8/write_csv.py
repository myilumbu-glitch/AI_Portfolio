import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["name", "grade", "age"])
    writer.writerow(["Alice", "A", 22])
    writer.writerow(["Bob", "B", 19])
    writer.writerow(["Charlie", "C", 46])

import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)

#using lists is more efficient
import csv

students = [
    ["name", "grade", "age"],
    ["Alice", "A", 20],
    ["Bob", "B", 22],
    ["Charlie", "C", 19]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for student in students:
        writer.writerow(student)