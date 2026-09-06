#line chart
from os import name

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]

plt.plot(x, y)

plt.title("My First Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

#bar chart
import matplotlib.pyplot as plt

names = ["A", "B", "C"]
scores = [80, 90, 85]

plt.bar(names, scores)

plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Score")

plt.show()

#histogram
import matplotlib.pyplot as plt

scores = [80, 90, 85, 70, 60, 75, 95, 88, 82, 91]

plt.hist(scores)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.show()


#Pandas + Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

df["score"].plot()

plt.show()

#Day5

import matplotlib.pyplot as plt
import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 120, 90, 150]

names = ["Ali", "Sara", "Maya", "John"]
scores = [90, 95, 88, 72]

all_scores = [90, 95, 88, 72, 80, 85, 91, 76, 89, 93]

#line chart
plt.plot(months,sales)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#bar chart
plt.bar(names, scores)
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

#histogram
plt.hist(all_scores)
plt.title("Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()


