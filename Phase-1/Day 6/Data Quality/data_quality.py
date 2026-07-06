import pandas as pd

df = pd.read_csv('dirty_students.csv')

# Step 1: Check for problems first
print("Number of missing values:")
print('-' * 30)
print(df.isnull().sum(),"\n")        # missing values per column

print("Number of duplicate rows:",df.duplicated().sum())    # count of duplicate rows

# Step 2: Fill missing values — sensibly, per column type
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
df['CGPA'] = df['CGPA'].fillna(df['CGPA'].mean())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())
df['Department'] = df['Department'].fillna('Unknown')

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

# Step 4: Reset index after dropping rows (good practice, mentioned in C9)
df = df.reset_index(drop=True)

# Step 5: Save the cleaned file
df.to_csv('cleaned_students.csv', index=False)
