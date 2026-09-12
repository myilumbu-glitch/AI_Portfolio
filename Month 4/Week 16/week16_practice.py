import pandas as pd
df = pd.read_csv("students_messy.csv")

print(df)
print(df.isna())
print(df.isna().sum())

clean_df = df.dropna() #removes columns with missing values
print(clean_df)

filled_df = df.fillna(0) #replaces the missing values with 0
print(filled_df)

average_score = df["score"].mean()
print("Average score:",average_score)

df["score"] = df["score"].fillna(average_score) #replaces the missing values with the average score
print(df)

#duplicates
import pandas as pd

df = pd.read_csv("students_duplicates.csv")

print(df)

print(df.duplicated())
#True means that the row is a duplicate, False means that the row is not a duplicate

clean_df = df.drop_duplicates() #removes the duplicate rows
print(clean_df)

#types of data
import pandas as pd

df = pd.read_csv("student_types.csv")

print(df)
print(df.dtypes)

df["score"] = df["score"].astype(int) #converts the score column to integer type
print(df.dtypes)

