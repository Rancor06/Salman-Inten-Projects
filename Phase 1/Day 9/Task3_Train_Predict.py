import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Same split as Task 2, so results stay consistent across tasks
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 3. Predict on the full test set
y_pred = model.predict(X_test)

# 4. Print actual values
print("===== ACTUAL VALUES (y_test) =====")
print(y_test)

# 5. Print predicted values
print("\n===== PREDICTED VALUES (y_pred) =====")
print(y_pred)

# 6. Compare both outputs side by side
comparison = pd.DataFrame({
    'Actual': [iris.target_names[i] for i in y_test],
    'Predicted': [iris.target_names[i] for i in y_pred],
    'Match': y_test == y_pred
})

print("\n===== SIDE-BY-SIDE COMPARISON =====")
print(comparison.to_string())

# Quick summary of how many predictions were correct
correct = comparison['Match'].sum()
total = len(comparison)
print(f"\nCorrect predictions: {correct}/{total}")
