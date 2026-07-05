#Create one dictionary: name, subject, score, status.
dets = {
    "name": "Salman",
    "subject": "Data Warehousing",
    "score": "85",
    "status": "Pass",
}

print("\nStudent Report")
print("-" * 30)

#Print each value using an f-string, one per line.
print(f"Name of the student: {dets['name']}")
print(f"Subject            : {dets['subject']}")
print(f"Score Recieved     : {dets['score']}")
print(f"Acceptance Status  : {dets['status']}")
print("-" * 30)

#Updated details
dets["score"] = 90
print("Score has been updated, the updated report is given below\n")

print("Student Report")
print("-" * 30)
print(f"Name of the student: {dets['name']}")
print(f"Subject            : {dets['subject']}")
print(f"Score Recieved     : {dets['score']}")
print(f"Acceptance Status  : {dets['status']}")
print("-" * 30)