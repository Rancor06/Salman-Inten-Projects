import pandas as pd

df = pd.read_csv('cleaned_students.csv')

# Step 1: Filter using ALL three conditions combined with &
eligible = df[(df['CGPA'] >= 8.5) & (df['Backlogs'] == 0) & (df['Attendance'] >= 90)]

# Q1: How many eligible?
num_eligible = len(eligible)

# Q2: Name, Department, CGPA of eligible students
eligible_details = eligible[['Name', 'Department', 'CGPA']]

# Q3: Most common department among eligible students
top_department = eligible['Department'].value_counts().idxmax()

# Q4: Average Marks — eligible vs whole class
avg_marks_eligible = eligible['Marks'].mean()
avg_marks_class = df['Marks'].mean()

print("SCHOLARSHIP SHORTLIST REPORT")
print(f"Total eligible students: {num_eligible}")
print(eligible_details)
print(f"Most represented department among eligible students: {top_department}")
print(f"Average Marks — Eligible: {avg_marks_eligible:.2f} | Whole Class: {avg_marks_class:.2f}\n")

# Step 5: Save the shortlist
eligible.to_csv('scholarship_shortlist.csv', index=False)