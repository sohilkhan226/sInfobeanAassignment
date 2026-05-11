# 2. University Admission System

# A university decides admission based on marks, entrance score, and category of the student.

# If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

# Input:
# Marks = 72
# Entrance Score = 85
# Category = general

# Output:
# Admission Status = Admitted

marks = int(input("Enter marks: "))
entrance_score = int(input("Enter entrance score: "))
category = input("Enter category: ").lower()

if marks >= 70:
    if entrance_score >= 80:
        if category == "general":
            status = "Admitted"
        else:
            status = "Admitted with Scholarship"
    else:
        if marks >= 85:
            status = "Admitted under Management Quota"
        else:
            status = "Rejected"
else:
    if category == "general":
        status = "Rejected"
    else:
        if marks >= 60:
            if entrance_score >= 70:
                status = "Waitlisted"
            else:
                status = "Rejected"
        else:
            status = "Rejected"

print("Admission Status =", status)