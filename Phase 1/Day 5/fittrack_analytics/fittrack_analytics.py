import numpy as np

days_steps = {}  # will hold {day_name: step_count}

# Step 2-4: safely read the file, parse each line, build dictionary
try:
    with open("steps_log.txt", "r") as f:
        for line in f:
            line = line.strip()  # remove newline/whitespace
            if line:  # skip any blank lines
                day, count = line.split(":")  # split "Monday:8500" into day + count
                days_steps[day] = int(count)  # store in dict, convert string to int
except FileNotFoundError:
    print("Error: steps_log.txt not found. Make sure it's in the same folder.")
    exit()  # stop the script if the file is missing

# Step 5: pull step counts into a NumPy array (keeping same order as dict)
days = list(days_steps.keys())
steps = np.array(list(days_steps.values()))

mean_steps = steps.mean()
max_steps = steps.max()
min_steps = steps.min()

# Step 6: normalize steps to a 0-1 scale (vectorized, no loop)
# formula: (value - min) / (max - min) -> smallest becomes 0, largest becomes 1
normalized = (steps - min_steps) / (max_steps - min_steps)

# Step 7: goal rate - % of days that hit 8000+ steps
# boolean mask (steps >= 8000) gives True/False per day, .sum() counts the Trues
goal_rate = np.sum(steps >= 8000) / len(steps) * 100

# Step 8: find best and worst day by name using argmax/argmin
# argmax/argmin return the INDEX of the max/min value, not the value itself
best_day = days[np.argmax(steps)]
worst_day = days[np.argmin(steps)]

# Step 9: rank all days from highest to lowest steps
# argsort gives indices that would sort ascending; [::-1] reverses it to descending
ranked_indices = np.argsort(steps)[::-1]

# Report
print("-" * 55)
print("FitTrack Analytics - Weekly Step Report")
print("-" * 55)

for day in days:
    idx = days.index(day)
    print(f"{day:<10}{steps[idx]:>6} steps   (normalized: {normalized[idx]:.2f})")

print("-" * 55)
print(f"{'Average steps:':<25}{mean_steps:>10.1f}")
print(f"{'Highest step count:':<25}{max_steps:>10} ({best_day})")
print(f"{'Lowest step count:':<25}{min_steps:>10} ({worst_day})")
print(f"{'Goal rate (8000+ steps):':<25}{goal_rate:>9.1f}%")
print("-" * 55)

print("Leaderboard (highest to lowest):")
for rank, idx in enumerate(ranked_indices, start=1):
    print(f"{rank}. {days[idx]:<10}{steps[idx]} steps")

print("-" * 55)