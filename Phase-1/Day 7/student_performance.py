import pandas as pd

# Step 1: Read the 3 CSV files
students = pd.read_csv("Students.csv")
results = pd.read_csv("Results.csv")
attendance = pd.read_csv("Attendance.csv")
students['Adm_No'] = students['Adm_No'].astype(str)
results['Adm_No'] = results['Adm_No'].astype(str)
attendance['Adm_No'] = attendance['Adm_No'].astype(str)

print("Students:", students.shape)
print("Results:", results.shape)
print("Attendance:", attendance.shape)

# Step 2: Filter Results to a specific Class / Term
TARGET_CLASS = "III"
TARGET_TERM = "Term1"

results_with_class = results.merge(
    students[['Adm_No', 'Term', 'Class']], on=['Adm_No', 'Term'], how='left'
)
results_filtered = results_with_class[
    (results_with_class['Class'] == TARGET_CLASS) & (results_with_class['Term'] == TARGET_TERM)
]
print(f"\nResults filtered to Class {TARGET_CLASS}, {TARGET_TERM}:", len(results_filtered))

# Step 3: Group by Adm_No - total & avg Marks per student
marks_summary = (
    results_filtered.groupby('Adm_No')['Marks']
    .agg(total_marks='sum', avg_marks='mean')
    .reset_index()
)
print("\nMarks summary (first 5):")
print(marks_summary.head())

# Step 4: Group Attendance by Adm_No, compute attendance %
attendance_summary = (
    attendance.groupby('Adm_No')['Status']
    .apply(lambda x: (x == 'Present').sum() / len(x) * 100)
    .reset_index(name='attendance_rate')
)
print("\nAttendance summary (first 5):")
print(attendance_summary.head())

# Step 5: Merge scores + attendance + Students -> final_report.csv
students_unique = students.drop(columns=['Term']).drop_duplicates('Adm_No')

final_report = students_unique.merge(marks_summary, on='Adm_No', how='left')
final_report = final_report.merge(attendance_summary, on='Adm_No', how='left')

final_report['avg_marks'] = final_report['avg_marks'].round(2)
final_report['attendance_rate'] = final_report['attendance_rate'].round(2)

final_report.to_csv("final_report.csv", index=False)
print("\nfinal_report.csv saved:", final_report.shape)

# Step 6: Filter attendance < 75% AND avg Marks < 40 -> at_risk.csv
at_risk = final_report[
    (final_report['attendance_rate'] < 75) & (final_report['avg_marks'] < 40)
]
at_risk.to_csv("at_risk.csv", index=False)
print("At-risk students flagged:", len(at_risk))

# ANSWERS TO THE SLIDE QUESTIONS
print("\n--- ANSWERS ---")

# Q1: Top 5 students by avg Marks and their attendance rates
top5 = final_report.sort_values('avg_marks', ascending=False).head(5)
print("Q1: Top 5 students by avg Marks:")
print(top5[['Adm_No', 'avg_marks', 'attendance_rate']])

# Q2: How many students flagged as at-risk?
print(f"Q2: {len(at_risk)} students flagged as at-risk.")

# Q3: How does missing Attendance bias attendance_rate?
print("""
Q3: If a student has NO rows at all in Attendance.csv, groupby() simply
never produces a row for them, and the merge leaves attendance_rate as
NaN rather than 0. If you don't handle that NaN, they'll be silently
EXCLUDED from the at-risk filter (since NaN < 75 evaluates to False),
even though missing attendance data should probably count as a red
flag, not a free pass. Fix: fillna(0) or flag NaN attendance separately
before applying the at-risk filter.
""")

# Q4: Export final_report.csv with Percentage rounded to 2dp
print("Q4: Already handled above via final_report['avg_marks'].round(2) "
      "and final_report['attendance_rate'].round(2) before to_csv().")

# Q5: Fix int vs str Adm_No type mismatch on merge
print("""
Q5: If Adm_No is read as int64 in one CSV and object/str in another
(e.g. due to a leading zero like '007' being stored as a string),
pandas merge() will fail to match those rows even though they "look"
the same. Fix by forcing a consistent dtype on all three DataFrames
BEFORE merging:
    df['Adm_No'] = df['Adm_No'].astype(str)
This is done at the top of Step 1 in this script.
""")