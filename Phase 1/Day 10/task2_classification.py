from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Load the Wine dataset
wine = load_wine()

print("=" * 60)
print("TASK 2: Wine Classification System")
print("=" * 60)
print(f"\nDataset shape: {wine.data.shape[0]} samples, {wine.data.shape[1]} features")
print(f"Target classes: {list(wine.target_names)}")

# 2. Separate Features (X) and Target (y)
X = wine.data
y = wine.target

# 3. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")

# 4. Train a Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("\nDecision Tree Classifier trained successfully.")

# 5. Predict the category for the testing dataset
y_pred = model.predict(X_test)
print("\nPredictions on test data:")
print(y_pred)

# 6. Print the model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")