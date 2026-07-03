def add(a, b):
    return a + b

print(add(4, 5))

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Salman"))
print(greet("Salman", "Welcome back"))

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([40, 10, 90, 25])
print(f"low={low} high={high}")
