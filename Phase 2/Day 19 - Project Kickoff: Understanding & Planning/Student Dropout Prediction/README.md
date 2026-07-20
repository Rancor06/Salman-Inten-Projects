# Student Dropout Risk Predictor

## Problem Statement
Predict whether a student will drop out, remain enrolled, or graduate, using data available at enrollment time and academic performance from the first two semesters. Early identification allows the institution to intervene before a student disengages entirely.

## Dataset Information
- **Name:** Predict Students' Dropout and Academic Success
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)
- **Rows:** 4,424
- **Columns:** 37 (36 features + 1 target)
- **Target Variable:** `Target` (Dropout / Enrolled / Graduate)

## Project Objectives
- Build a classification model that flags at-risk students early using enrollment and early-semester data.
- Identify the strongest predictive features (e.g., admission grade, first-semester units approved, socio-economic indicators).
- Handle class imbalance across the three target categories in a way that keeps minority-class (Dropout) performance meaningful, not just overall accuracy.

## Technologies Used
- Python
- Pandas, NumPy
- scikit-learn (DecisionTreeClassifier)
- Google Colab / Jupyter Notebook

## Planned Workflow
1. Data loading and initial exploration (data types, missing values, summary statistics)
2. Preprocessing (identifying numerically-coded categorical fields — e.g., Marital status, Course, Gender, Debtor are stored as integer codes rather than text, so dtype alone doesn't separate true categorical vs numerical features; cross-checking against the UCI feature dictionary before deciding on encoding)
3. Feature engineering (e.g., pass-rate ratios)
4. Model training with a Decision Tree Classifier
5. Evaluation using accuracy, precision, recall, and F1-score (weighted, given class imbalance)
6. Documentation and iteration
