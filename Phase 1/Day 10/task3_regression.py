import pickle
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Load the Diabetes dataset
diabetes = load_diabetes()

print("=" * 60)
print("TASK 3: Healthcare Prediction & Model Saving")
print("=" * 60)
print(f"\nDataset shape: {diabetes.data.shape[0]} samples, {diabetes.data.shape[1]} features")
print(f"Features: {diabetes.feature_names}")
print("Target: quantitative measure of disease progression one year after baseline")

# 2. Separate Features (X) and Target (y)
X = diabetes.data
y = diabetes.target

# 3. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")

# 4. Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("\nLinear Regression model trained successfully.")

# 5. Predict the testing dataset
y_pred = model.predict(X_test)

# 6. Print the Actual and Predicted values
print("\nActual vs Predicted (first 10 test samples):")
print(f"{'Actual':>10} {'Predicted':>12}")
for actual, predicted in zip(y_test[:10], y_pred[:10]):
    print(f"{actual:>10.1f} {predicted:>12.1f}")

# 7. Calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error (MSE): {mse:.2f}")

# 8. Save the trained model as diabetes_model.pkl
with open('diabetes_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("\nModel saved successfully as 'diabetes_model.pkl'")