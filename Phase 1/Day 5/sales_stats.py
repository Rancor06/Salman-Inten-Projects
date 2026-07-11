import numpy as np

sales = np.array([1245,2890,3476,4125,5983,7214,8657])
mean_sales = sales.mean()
max_sales = sales.max()
min_sales = sales.min()
total_sales = sales.sum()
abv_avg =   (sales > mean_sales).sum()

print("-" * 50)
print("Sales Report — Weekly Performance Overview")
print("-" * 50)
print(f"{'Mean sales for the week:':<40}{mean_sales:>6.2f}")
print(f"{'Minimum sale amount in the week:':<40}{min_sales:>6}")
print(f"{'Maximum sale amount in the week:':<40}{max_sales:>6}")
print(f"{'Number of days above average sale:':<40}{abv_avg:>6}")
print(f"{'Week sale total:':<40}{total_sales:>6}")
print("-" * 50)