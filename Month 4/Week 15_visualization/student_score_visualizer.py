#miniproject
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv") #“Read students.csv and store the resulting DataFrame in the variable df.”

print(df) 

average = df["score"].mean()
print("Average score:", average)

plt.bar(df["name"], df["score"])
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Score")

plt.savefig("student_scores.png") #saves bar chart as a png file
plt.show() 
