import pandas as pd

# Step 1: Read CSV, display info (dtypes, missing counts)
df = pd.read_csv("Exam_scores.csv")

print("Info:")
df.info()                       # shows dtypes + non-null counts per column
print("\nMissing values per column:")
print(df.isnull().sum())        # explicit count of NaNs per column

# Step 2: Fill missing Marks with subject-wise mean
missing_before = df['Marks'].isnull().sum()

subject_means = df.groupby('Subject')['Marks'].transform('mean')
df['Marks'] = df['Marks'].fillna(subject_means)
print(f"\nFilled {missing_before} missing Marks values using each subject's mean.")

# Step 3: Group by Subject - count, mean, min, max Marks
subject_stats = df.groupby('Subject')['Marks'].agg(['count', 'mean', 'min', 'max'])
print("\nSubject-wise stats:")
print(subject_stats)

# Step 4: Group by Class, compute average Marks
class_avg = df.groupby('Class')['Marks'].mean()
print("\nClass-wise average Marks:")
print(class_avg)

# Step 5: Top 3 students by total marks (groupby + sum)
top3 = (
    df.groupby('Adm_No')['Marks']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
print("\nTop 3 students by total marks:")
print(top3)

# ANSWERS TO THE SLIDE QUESTIONS
print("\n--- ANSWERS ---")

# Q1: How many missing Marks were filled and with what values?
print(f"Q1: {missing_before} missing values were filled, each with its "
      f"subject's mean Marks (values vary per subject, see subject_means).")

# Q2: Which subject has the highest mean Marks?
top_subject = subject_stats['mean'].idxmax()
print(f"Q2: Highest mean Marks subject = {top_subject} "
      f"({round(subject_stats['mean'].max(), 2)})")

# Q3: Code to flatten a multi-aggregation result
print("""
Q3: Flattening a multi-agg result (e.g. from the slide's example):
    result = df.groupby('city').agg({'salary': ['mean', 'sum']})
    result.columns = ['_'.join(col) for col in result.columns]
    result = result.reset_index()
This joins the (column, aggfunc) tuple column names into single strings
like 'salary_mean', 'salary_sum'.
""")

# Q4: Why is reset_index() necessary after groupby?
print("""
Q4: groupby() results use the grouped column(s) as the INDEX, not as a
regular column. reset_index() converts that index back into a normal
column, which is needed if you want to merge the result with another
DataFrame, export it to CSV cleanly, or keep using column-based syntax
like result['Subject'] instead of result.index.
""")
