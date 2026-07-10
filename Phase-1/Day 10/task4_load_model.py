import pickle
import numpy as np

print("=" * 60)
print("TASK 4: Reuse the Saved Model")
print("=" * 60)

# 1. Load the saved diabetes_model.pkl file
with open('diabetes_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

print("\nModel loaded successfully from 'diabetes_model.pkl'")
print(f"Model type: {type(loaded_model).__name__}")

# 2. Predict the disease progression for a new patient
new_patient = np.array([[0.05, 0.05, 0.06, 0.02, -0.04, -0.03, -0.02, 0.03, 0.02, 0.01]])

print("\nNew patient feature values (age, sex, bmi, bp, s1-s6):")
print(new_patient)

# 3. Print the predicted value
predicted_progression = loaded_model.predict(new_patient)
print(f"\nPredicted disease progression score: {predicted_progression[0]:.2f}")

# 4. Verify that prediction works without retraining
print("\nVerification: No model.fit() was called in this script.")
print("The model used above was trained once in Task 3 and reused here")
print("purely by loading it from disk - this is the core idea behind")
print("saving and deploying ML models in real applications.")