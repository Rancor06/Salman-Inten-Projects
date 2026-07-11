import pandas as pd

df = pd.read_csv('students.csv')

# Q1: Marks > 80 AND Backlogs == 0
shortlist1 = df[(df['Marks'] > 80) & (df['Backlogs'] == 0)]
print("\nStudents with Marks > 80 & Backlogs == 0")
print("-" * 60)
print(shortlist1)

# Q2: Department == 'CSE' AND Year == 3
shortlist2 = df[(df['Department'] == 'CSE') & (df['Year'] == 3)]
print("\nStudents in Department == 'CSE' & Year == 3")
print("-" * 60)
print(shortlist2)

# Q3: CGPA above class average
class_avg_cgpa = df['CGPA'].mean()
shortlist3 = df[df['CGPA'] > class_avg_cgpa]
print("\nStudents with CGPA above class average")
print("-" * 60)
print(shortlist3,"\n")