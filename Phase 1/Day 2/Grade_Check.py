print("========== Grade Checker ==========")

score = int(input("Enter Score:"))
if score > 100 or score < 0:
    print("Invalid Score")
else:
    if score <= 100 and score >= 90:
        print("You have recived A Grade")
    elif score < 90 and score >= 75:
        print("You have recived B Grade")
    elif score < 75 and score >= 50:
        print("You have recived C Grade")
    else:
        print("You have failed")
    
print("===================================")