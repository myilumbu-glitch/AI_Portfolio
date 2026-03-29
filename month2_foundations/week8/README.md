# CSV Cleaner Project

## Description

This Python project reads a messy CSV file, cleans the data, and writes the cleaned data into a new CSV file.

## Features

* Reads CSV files
* Removes extra spaces
* Converts text to lowercase
* Saves cleaned data to a new CSV file

## Files

* `read_csv.py` → practice reading CSV files
* `write_csv.py` → practice writing CSV files
* `csv_cleaner.py` → final project
* `messy_students.csv` → raw input file
* `clean_students.csv` → cleaned output file

## How to Run

1. Open terminal in the project folder
2. Run:

```bash
python csv_cleaner.py
```

## Example

### Input:

```csv
name,grade
 Alice , A
bob,B
 CHARLIE , c
```

### Output:

```csv
name,grade
alice,a
bob,b
charlie,c
```

## Technologies Used

* Python
* CSV module
