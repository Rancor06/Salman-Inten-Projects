# 1. Import pandas and sklearn
import pandas as pd
from sklearn.datasets import load_iris

# 2. Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 3. Print the complete dataset
print("===== FULL DATASET =====")
print(df.to_string())

# 4. Filter rows where Sepal Length > 5.0
print("\n===== ROWS WHERE SEPAL LENGTH > 5.0 =====")
filtered_df = df[df['sepal length (cm)'] > 5.0]
print(filtered_df.to_string())

# 5. Display only Sepal Length and Petal Length
print("\n===== SEPAL LENGTH & PETAL LENGTH ONLY =====")
print(df[['sepal length (cm)', 'petal length (cm)']].to_string())

# 6. Check for missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 7. Print summary statistics
print("\n===== SUMMARY STATISTICS (describe) =====")
print(df.describe())

# 8. Display data types
print("\n===== DATA TYPES =====")
print(df.dtypes)
print("\n===== INFO =====")
print(df.info())

# 9. Save the dataset as iris_dataset.csv
df.to_csv('iris_dataset.csv', index=False)
print("\nSaved dataset as iris_dataset.csv")
