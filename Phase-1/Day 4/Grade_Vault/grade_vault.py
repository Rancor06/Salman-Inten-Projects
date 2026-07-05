from grade_utils import PASS_CUTOFFS

# 1. List of dictionaries -- 5 students across 2 subjects
students = [
    {"name": "Aditi", "subject": "Python", "score": 82, "status": "Distinction"},
    {"name": "Rahul", "subject": "Python", "score": 58, "status": "Pass"},
    {"name": "Meena", "subject": "DSA", "score": 30, "status": "Fail"},
    {"name": "Karthik", "subject": "DSA", "score": 91, "status": "Distinction"},
    {"name": "Fatima", "subject": "Python", "score": 45, "status": "Pass"},
]

def unique_subjects():
    # Pull every subject out of the class, using a set to auto-remove duplicates.
    return {s["subject"] for s in students}

def add_student(name, subject, score):
    # Decide status by checking the score against the locked cutoffs tuple.
    if score < PASS_CUTOFFS[0]:
        status = "Fail"
    elif score < PASS_CUTOFFS[2]:
        status = "Pass"
    else:
        status = "Distinction"

    # Build the new record and add it to the class list.
    new_student = {"name": name, "subject": subject, "score": score, "status": status}
    students.append(new_student)

    # Log the addition to a text file so there's a persistent record.
    with open("grades_log.txt", "a") as f:
        f.write(f"Added: {name} | {subject} | {score} | {status}\n")

    print(f"Added {name} to the class with status: {status}")

def list_students():
    print("===== GRADEVAULT =====")
    for s in students:
        print(f"{s['name']} | {s['subject']} | {s['score']} | {s['status']}")
    print("=========================")

def class_average(subject):
    scores = [s["score"] for s in students if s["subject"] == subject]
    if not scores:
        return 0
    return sum(scores) / len(scores)

def top_scorer():
    best = students[0]
    for s in students:
        if s["score"] > best["score"]:
            best = s
    return best

def search_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return "Not found"

def top_scorers():
    return [s["name"] for s in students if s["status"] == "Distinction"]

if __name__ == "__main__":
    list_students()
    print(f"Unique subjects: {unique_subjects()}")
    print(f"Pass cutoffs (locked): {PASS_CUTOFFS}")

    add_student("Divya", "DSA", 60)
    print(f"Python class average: {class_average('Python')}")
    print(f"Top scorer: {top_scorer()}")
    print(f"Search 'Meena': {search_student('Meena')}")
    print(f"Search 'Zara': {search_student('Zara')}")
    print(f"Distinction students: {top_scorers()}")