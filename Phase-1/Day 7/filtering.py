import pandas as pd

# Step 1: Read CSV, show shape and first 5 rows
df = pd.read_csv("Student_results.csv")

print("Shape (rows, cols):", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Step 2: Create a Series of all Percentage values
percentage_series = df['Percentage']
print("\nType check:", type(percentage_series))   # <class 'pandas.core.series.Series'>
print(percentage_series.head())

# Step 3: Filter Percentage >= 75, save to filtered_high.csv
filtered_high = df[df['Percentage'] >= 75]
filtered_high.to_csv("filtered_high.csv", index=False)
print("\nStudents with Percentage >= 75:", len(filtered_high))

# Step 4: Filter Maths rows with Marks < 40, display count
maths_fail = df[(df['Subject'] == 'Maths') & (df['Marks'] < 40)]
print("\nMaths students scoring below 40:", len(maths_fail))
print(maths_fail[['Adm_No', 'Name', 'Marks']] if 'Name' in df.columns else maths_fail)

# Step 5: Use .query() for female Class II students with Percentage > 60
female_class2_high = df.query("Gender == 'Female' and Class == 'II' and Percentage > 60")
print("\nFemale Class II students with Percentage > 60:")
print(female_class2_high)

# ANSWERS TO THE SLIDE QUESTIONS
print("\n--- ANSWERS ---")

# Q1: How many students have Percentage >= 75?
print("Q1:", len(filtered_high), "students have Percentage >= 75")

# Q2: What is the average Percentage of the high-% group?
print("Q2: Average Percentage of that group =", round(filtered_high['Percentage'].mean(), 2))

# Q3: Which student(s) in Maths scored below 40?
print("Q3: Maths students below 40 marks:")
print(maths_fail)

# Q4: .loc vs .iloc for filtering
print("""
Q4:
- .loc  -> label-based selection. You use COLUMN NAMES and INDEX LABELS.
           e.g. df.loc[df['Marks'] < 40, ['Name', 'Marks']]
           Also used for boolean filtering combined with column selection.
- .iloc -> position-based (integer index) selection. You use ROW/COLUMN
           NUMBERS, e.g. df.iloc[0:5, 1:3] gets first 5 rows, columns 1-2.
- It is recommended to use .loc when you know the column NAME or want to filter
  with a boolean condition and use .iloc when you only know the POSITION.
""")
