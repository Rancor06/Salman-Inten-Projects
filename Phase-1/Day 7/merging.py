"""
TASK 3 - MERGING
Datasets: Students.csv + Results.csv
Expected join key: Adm_No (and Term for the multi-key merge)
"""

import pandas as pd

# -----------------------------------------------------------------
# Step 1: Read both CSVs, inspect keys and duplicates
# -----------------------------------------------------------------
students = pd.read_csv("Students.csv")
results = pd.read_csv("Results.csv")

print("Students shape:", students.shape)
print("Results shape:", results.shape)

print("\nDuplicate Adm_No in Students:", students['Adm_No'].duplicated().sum())
print("Duplicate Adm_No in Results:", results['Adm_No'].duplicated().sum())

# -----------------------------------------------------------------
# Step 2: Inner merge on Adm_No, save as inner_merge.csv
# -----------------------------------------------------------------
# Inner join keeps ONLY rows where Adm_No exists in BOTH DataFrames.
inner_merge = pd.merge(students, results, on='Adm_No', how='inner')
inner_merge.to_csv("inner_merge.csv", index=False)
print("\nInner merge rows:", len(inner_merge))

# -----------------------------------------------------------------
# Step 3: Left merge, identify students without results
# -----------------------------------------------------------------
# Left join keeps ALL rows from `students`, filling NaN where there's
# no matching row in `results`.
left_merge = pd.merge(students, results, on='Adm_No', how='left')

# indicator=True adds a "_merge" column showing where each row came from,
# which makes it easy to isolate students with no match in results.
merge_check = pd.merge(students, results, on='Adm_No', how='left', indicator=True)
no_results = merge_check[merge_check['_merge'] == 'left_only']
print("\nStudents with no results:", len(no_results))
print(no_results[['Adm_No']])

# -----------------------------------------------------------------
# Step 4: Outer merge, fill NaNs (-1 or "No Result")
# -----------------------------------------------------------------
# Outer join keeps every row from BOTH tables, matching where possible.
outer_merge = pd.merge(students, results, on='Adm_No', how='outer')

# Fill numeric result columns with -1 and text columns with "No Result".
# Adjust column names below to match your actual Results.csv columns.
if 'Marks' in outer_merge.columns:
    outer_merge['Marks'] = outer_merge['Marks'].fillna(-1)
if 'Grade' in outer_merge.columns:
    outer_merge['Grade'] = outer_merge['Grade'].fillna("No Result")

print("\nOuter merge rows:", len(outer_merge))

# -----------------------------------------------------------------
# Step 5: Merge on multiple keys (Adm_No + Term)
# -----------------------------------------------------------------
# Pass a list to `on` when the match depends on more than one column,
# e.g. a student can appear multiple times, once per Term.
multi_key_merge = pd.merge(students, results, on=['Adm_No', 'Term'], how='inner')
print("\nMulti-key merge rows:", len(multi_key_merge))

# ===================================================================
# ANSWERS TO THE SLIDE QUESTIONS
# ===================================================================
print("\n--- ANSWERS ---")

# Q1: How many rows differ between inner and left merge?
diff = len(left_merge) - len(inner_merge)
print(f"Q1: Left merge has {diff} more rows than inner merge "
      f"(students with no matching result).")

# Q2: Code to rename duplicate columns from merge
print("""
Q2: When both DataFrames share a non-key column name (e.g. 'Name'),
pandas auto-suffixes them as Name_x / Name_y. To rename explicitly:
    merged = pd.merge(students, results, on='Adm_No', suffixes=('_student', '_result'))
Or rename after merging:
    merged = merged.rename(columns={'Name_x': 'Student_Name', 'Name_y': 'Result_Name'})
""")

# Q3: Outer vs left merge - when to use which
print("""
Q3:
- Use LEFT merge when you have one "primary" table (e.g. all enrolled
  students) and want to keep every row from it, adding info from the
  other table only where it exists.
- Use OUTER merge when neither table is "primary" and you want to see
  EVERY record from both sides, including rows that don't match
  anywhere (useful for finding orphaned records on either side).
""")

# Q4: If Adm_No is duplicated in Results, how does inner merge affect row counts?
print("""
Q4: If Adm_No appears multiple times in Results (e.g. one row per Term),
an inner merge produces a CARTESIAN-style expansion: each Student row
gets duplicated once per matching Adm_No in Results. So the merged
row count can be GREATER than the original Students row count, not
just equal to the number of matching students.
""")