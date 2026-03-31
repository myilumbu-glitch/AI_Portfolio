import csv

cleaner = []

with open("messy_students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        cleaned_items = []

        for item in row:
            cleaned_item = item.strip().lower()
            cleaned_items.append(cleaned_item)
        cleaner.append(cleaned_items)

with open("cleaned_students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    for row in cleaner:
        writer.writerow(row)


print("CSV file successfully cleaned!")
