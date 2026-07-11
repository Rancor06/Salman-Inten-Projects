import numpy as np

raw_scores = np.array([55, 62, 48, 70, 58, 65])
curved_scores = raw_scores + 4 #curve of 4 points
original_mean = raw_scores.mean()
curved_mean = curved_scores.mean()

print("Class Score Report: Before & After Curve (by 4)")
print("-" * 57)

for i in range(len(raw_scores)):
    print(f"Original Score: {raw_scores[i]}\tCurved Score: {curved_scores[i]}")
print(f"\nOriginal Score Mean: {original_mean:.2f}\t Curved Score Mean: {curved_mean:.2f}")
print("-" * 57)