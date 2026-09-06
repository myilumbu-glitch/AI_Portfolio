# Student Score Visualizer

A simple Python project that loads student scores from a CSV file, calculates the average score using Pandas, and visualizes the scores using Matplotlib.

## Project Overview

This project demonstrates how to combine **Pandas** and **Matplotlib** to analyze and visualize data.

The program:

* Loads student data from a CSV file
* Stores the data in a Pandas DataFrame
* Calculates the average student score
* Creates a bar chart comparing student scores
* Adds a title and axis labels to the chart
* Saves the visualization as a PNG image

## Technologies Used

* Python
* Pandas
* Matplotlib
* CSV

## Example Dataset

The project uses a `students.csv` file containing:

| Name | Score | Age |
| ---- | ----: | --: |
| Ali  |    90 |  18 |
| Sara |    95 |  19 |
| John |    70 |  17 |
| Maya |    88 |  18 |

The calculated average score is **85.75**.

## How It Works

The CSV file is loaded using Pandas:

```python
df = pd.read_csv("students.csv")
```

The score column is selected and its average is calculated:

```python
average = df["score"].mean()
```

The scores are then visualized using a bar chart:

```python
plt.bar(df["name"], df["score"])
```

The chart is saved using:

```python
plt.savefig("student_scores.png")
```

## What I Learned

Through this project, I practiced:

* Loading CSV data with Pandas
* Working with DataFrames and Series
* Selecting columns from a DataFrame
* Calculating statistics with `.mean()`
* Creating bar charts with Matplotlib
* Adding titles and axis labels
* Saving visualizations as image files
* Combining data analysis and visualization into one Python program

## Files

```text
week15_visualization/
├── students.csv
├── student_score_visualizer.py
├── student_scores.png
└── README.md
```

## Goal

This project is part of my Python and AI foundations learning journey. It builds my understanding of how raw data can be **loaded, analyzed, and communicated visually**.
