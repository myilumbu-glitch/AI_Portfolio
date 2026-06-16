import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Print summary
print("Dataset Summary:")
print(df.describe())

# Filter students
high_scores = df[df["score"] > 85]

print("\nTop Students:")
print(high_scores[["name", "score"]])

# Calculate average
average = df["score"].mean()

print("\nAverage score:", average)



Dataset Summary:
...
 
Top Students:
name   score
Ali    90
Sara   95
Maya   88

Average score: 85.75
