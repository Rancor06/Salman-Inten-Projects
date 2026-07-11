import pandas as pd
from sklearn.datasets import load_iris

# 1. Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("=" * 60)
print("TASK 1: Iris Dataset Exploration")
print("=" * 60)

# 2. Display the first 5 rows
print("\n[1] First 5 rows of the dataset:")
print(df.head())

# 3. Find total number of flowers in each species
print("\n[2] Total number of flowers in each species:")
species_count = df['species'].value_counts()
print(species_count)

# 4. Find the average value of all features for each species
print("\n[3] Average value of all features for each species:")
species_avg = df.groupby('species', observed=True).mean(numeric_only=True)
print(species_avg)

# 5. Display all Virginica flowers whose Petal Length >
#    dataset average petal length
avg_petal_length = df['petal length (cm)'].mean()
print(f"\n[4] Dataset average petal length: {avg_petal_length:.2f} cm")

virginica_above_avg = df[
    (df['species'] == 'virginica') &
    (df['petal length (cm)'] > avg_petal_length)
]
print(f"Virginica flowers with Petal Length > {avg_petal_length:.2f} cm:")
print(virginica_above_avg)

# 6. Find the species with the highest average Sepal Length
highest_sepal_species = species_avg['sepal length (cm)'].idxmax()
print(f"\n[5] Species with the highest average Sepal Length: {highest_sepal_species}")
print(f"    (Average Sepal Length = {species_avg['sepal length (cm)'].max():.2f} cm)")

# 7. Create a new column: Sepal Area (Sepal Length x Sepal Width)
df['sepal area (cm^2)'] = df['sepal length (cm)'] * df['sepal width (cm)']
print("\n[6] Added 'sepal area (cm^2)' column. Preview:")
print(df[['sepal length (cm)', 'sepal width (cm)', 'sepal area (cm^2)']].head())

# 8. Save the required data as filtered_iris.csv
df.to_csv('filtered_iris.csv', index=False)
print("\n[7] Full dataset (with Sepal Area column) saved as 'filtered_iris.csv'")