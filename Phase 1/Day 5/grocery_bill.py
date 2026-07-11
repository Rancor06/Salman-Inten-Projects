import numpy as np

items = ["Rice","Milk","Eggs","Bread","Oil"]
prices = np.array([100, 25, 6, 50, 120])
quantity = np.array([3, 2, 5, 1, 2])
line_totals = prices * quantity

for i in range (len(items)):
    print(f"{items[i]}\tPrice(per unit): {prices[i]}\tQuantity: {quantity[i]}\tTotal Cost: {line_totals[i]}")

grand_total = line_totals.sum()
print(f"Pay a grand total of {grand_total} Rupees\n")