from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Same split as Tasks 2 & 3, for consistency
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# 1. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# 2. Print the accuracy score
print("===== ACCURACY SCORE =====")
print(f"{accuracy:.4f}  ({accuracy * 100:.2f}%)")

# 3. Print confusion matrix
print("\n===== CONFUSION MATRIX =====")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f"(rows = actual, columns = predicted, order = {list(iris.target_names)})")

# 4. Print classification report
print("\n===== CLASSIFICATION REPORT =====")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
