from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data          # features: sepal length, sepal width, petal length, petal width
y = iris.target        # target: 0=setosa, 1=versicolor, 2=virginica

# 2. Split into train/test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train a Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Predict the class for 2 sample inputs
# Format: [sepal length, sepal width, petal length, petal width]
sample_1 = [5.0, 3.4, 1.5, 0.2]   # looks like a setosa
sample_2 = [6.7, 3.1, 4.7, 1.5]   # looks like a versicolor

samples = [sample_1, sample_2]
predictions = model.predict(samples)

# 5. Print predicted flower names
print("===== SAMPLE PREDICTIONS =====")
for sample, pred in zip(samples, predictions):
    species_name = iris.target_names[pred]
    print(f"Input: {sample}  ->  Predicted species: {species_name}")