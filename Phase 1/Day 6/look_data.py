import pandas as pd

df = pd.read_csv('students.csv')

df.shape        # (rows, columns) — answers Q1
print(df.columns)      # list of column names — answers Q2
print(df.info())       # dtype of each column + non-null counts — answers Q3
print(df.head())       # first 5 rows — answers Q4
print(df.tail())       # last 5 rows — answers Q4