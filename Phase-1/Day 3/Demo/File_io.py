with open("notes.txt", "w") as f:
    f.write("First line\nSecond line\n")

with open("notes.txt", "r") as f:
    print(f.read())

with open("notes.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())

with open("notes.txt", "a") as f:
    f.write("Third line, added later\n")

try:
    with open("does_not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("That file doesn't exist yet -- handled gracefully.")