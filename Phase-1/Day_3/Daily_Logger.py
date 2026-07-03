from datetime import datetime

def add_entry(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.txt", "a") as f:
        f.write(f"[{timestamp}] {text}\n")

def show_entries():
    with open("journal.txt", "r") as f:
        for line in f:
            print(line.strip())

# Call add_entry three times with different text
add_entry("Woke up early and went for a run")
add_entry("Finished the Python practice round 1")
add_entry("Feeling good about today's progress")

# Then show all entries
show_entries()