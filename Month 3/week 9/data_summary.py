import csv

scores = []
ages = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        print("Processing row:", row)

        scores.append(int(row[2]))
        ages.append(int(row[1]))


# calculations
total_students = len(scores)
average_score = sum(scores) / len(scores)
average_age = sum(ages) / len(ages)
highest_score = max(scores)
lowest_score = min(scores)

# output
print("\n--- Student Data Summary ---")
print("Total students:", total_students)
print("Average score:", round(average_score, 2)) #showing only 2 decimal places
print("Average age:", round(average_age, 2)) #showing only 2 decimal places
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

#an improvement to handle missing scores. basically if empty skip, not then proccess normally.
if row[2] != "":
    scores.append(int(row[2]))
if row[1] != "":
    ages.append(int(row[1]))

#even better version;
try:
    score = int(row[2])
    scores.append(score)
except:
    print("Skipping invalid row:", row)


#Improved Version
import csv

scores = []
ages = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        try:
            if row[2] != "":
                score = int(row[2])
                scores.append(score)
        except:
            print("Skipping invalid row:", row)
        try:
            if row[1] != "":
                age = int(row[1])
                ages.append(age)
        except:
            print("Skipping invalid row:", row)


# calculations
total_students = len(scores)

if total_students > 0:
    average_score = sum(scores) / total_students
    average_age = sum(ages) / len(ages)
    highest_score = max(scores)
    lowest_score = min(scores)

    print("\n--- Student Data Summary ---")
    print(f"Total students: {total_students}")
    print(f"Average score: {round(average_score, 2)}")
    print(f"Average age: {round(average_age, 2)}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
else:
    print("No valid data found.")
