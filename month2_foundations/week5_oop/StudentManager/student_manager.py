# Student Manager Application. End of OOP concepts. This application allows you to manage a list of students, 
# including adding, removing, finding, and displaying student information. (07.03.26)


class Student:

    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade}"


class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added.")

    def remove_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Student removed.")
                return
        print("Student not found.")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print(s)
                return
        print("Student not found.")

    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for s in self.students:
                print(s)

manager = StudentManager()

s1 = Student("Alice", 101, "A")
s2 = Student("Bob", 102, "B")

manager.add_student(s1)
manager.add_student(s2)

manager.display_students()

manager.find_student(101)

manager.remove_student(102)

manager.display_students()