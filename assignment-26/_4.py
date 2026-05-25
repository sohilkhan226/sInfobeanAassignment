# 4.
# Employee ID Validator

# A company wants to validate employee IDs before storing them in the database.

# Conditions:
# - ID must start with "EMP"
# - Total length should be 8
# - Remaining characters should be digits only

# Input:
# Enter Employee ID: EMP10234

# Output:
# Valid Employee ID


emp_id = input("Enter Employee ID: ")

valid = True

# Check starts with EMP
if len(emp_id) == 8 and emp_id[:3] == "EMP":
    for ch in emp_id[3:]:
        if not ch.isdigit():
            valid = False
            break
else:
    valid = False

if valid:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")

