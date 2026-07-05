import numpy as np

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
celsius = np.array([7,18,24,31,42,13,36])
fahrenheit = celsius *9/5 + 32
print("Weekly Temperature Report (°C to °F)")
print("-" * 50)
for i in range(len(celsius)):
    print(f"{days[i]:<10}{celsius[i]:>3}C   ->   {fahrenheit[i]:>6.1f}F")
print("-" * 50)