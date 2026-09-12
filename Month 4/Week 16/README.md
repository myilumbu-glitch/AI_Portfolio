# Week 16 — Data Cleaning & Real-World Data

## 🎯 Goal

Learn how to identify and clean common problems in real-world datasets using Pandas.

## 📚 What I Learned

This week I learned how to:

* Detect missing values with `isna()`
* Count missing values with `isna().sum()`
* Remove missing data with `dropna()`
* Fill missing data with `fillna()`
* Calculate averages and medians
* Detect duplicate rows with `duplicated()`
* Remove duplicates with `drop_duplicates()`
* Check column data types with `dtypes`
* Convert data types with `astype()`
* Reset DataFrame indexes with `reset_index()`
* Save cleaned data with `to_csv()`

## 🧹 Mini Project — Student Data Cleaning

For the mini project, I worked with a deliberately messy student dataset containing:

* Missing student scores
* A missing age
* A duplicate student record
* Different data types

I used Pandas to clean the dataset and created a new cleaned CSV file.

### Cleaning Process

```text
Messy CSV
    ↓
Check missing values
    ↓
Remove duplicate records
    ↓
Calculate average score
    ↓
Fill missing scores
    ↓
Calculate and fill missing age
    ↓
Reset index
    ↓
Fix data types
    ↓
Validate cleaned data
    ↓
Save cleaned CSV
```

## 📁 Project Files

* `data_cleaning.py` — Python script used to clean the data
* `students_messy_final.csv` — Original messy dataset
* `students_cleaned.csv` — Final cleaned dataset

## 🧠 Key Takeaway

I learned that data cleaning is an important step before analysis or machine learning. Models and analyses depend on the quality of the data they receive, so understanding how to identify and handle messy data is an important foundation for AI and data science.
