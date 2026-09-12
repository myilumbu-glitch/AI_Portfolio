print("I AM RUNNING DATA_CLEANING.PY")

import pandas as pd

df = pd.read_csv("students_messy_final.csv")

print(df)

print(df.isna().sum())

df = df.drop_duplicates()

print(df)

average_score = df["score"].mean()

print("Average score:", average_score)

df["score"] = df["score"].fillna(average_score)

print(df)


median_age = df["age"].median()

print("Median age:", median_age)

df["age"] = df["age"].fillna(median_age)

print(df)

df = df.reset_index(drop=True)

print(df)

print(df.isna().sum())
print(df.duplicated().sum())
print(df.dtypes)

df["age"] = df["age"].astype(int)
print(df.dtypes)

df.to_csv("students_cleaned.csv", index=False)