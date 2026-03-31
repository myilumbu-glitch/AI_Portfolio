import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)

  
    for row in reader:
        print("Name:", row[0], " | Grade:", row[1])


import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader) # Skip the header row

    for row in reader:
        print("Name:", row[0], " | Grade:", row[1], " | Age:", row[2])

import csv
with open("products.csv", "r") as file:
    reader = csv.reader(file)

    next(reader) #skip header row

    for product in reader:
        print(product)
        

#Or using lists is more efficient
import csv
products = [
    ["product", "price", "quantity"],
    ["Phone", 500, 10],
    ["Laptop", 1200, 5],
    ["Mouse", 25, 20]
]

with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for product in products:
        writer.writerow(product)

with open("products.csv", "r") as file:
    reader = csv.reader(file)

    next(reader) #skip header row

    for product in reader:
        print("Product:", product[0], " | Price:", product[1], " | Quantity:", product[2])