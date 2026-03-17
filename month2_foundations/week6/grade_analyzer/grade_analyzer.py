import json
grades = [90, 85, 64, 72, 100]


def save_grades(grades):
    with open("grades.json", "w") as file:
        json.dump(grades, file)

def load_grades():
    try:
        with open("grades.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def analyze_grades(grades):
    if not grades:
        print("No grades available.")
        return

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print(f"Grades: {grades}")
    print(f"Average: {average}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


# MAIN Test the functions
grades = load_grades()

grades.append(88)   # simulate adding a grade 
grades.append(95)

save_grades(grades)

analyze_grades(grades)
