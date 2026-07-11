import pandas as pd

df = pd.read_csv('students.csv')

# Q1: Who scored the highest Marks?
top_scorer = df.loc[df['Marks'].idxmax(), 'Name']
print("Highest Marks:", top_scorer)

# Q2: Average CGPA
avg_cgpa = df['CGPA'].mean()
print("Average CGPA:", avg_cgpa)

# Q3: Best Attendance
best_attendance_student = df.loc[df['Attendance'].idxmax(), 'Name']
print("Best Attendance:", best_attendance_student)

# Q4: Average Attendance
avg_attendance = df['Attendance'].mean()
print("Average Attendance:", avg_attendance)