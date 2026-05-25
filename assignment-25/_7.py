# 7.
# Vehicle Number Plate Checker

# The traffic department wants to validate vehicle registration numbers.

# Conditions:
# - First 2 characters should be alphabets
# - Next 2 should be digits
# - Total length should be 10

# Input:
# Enter vehicle number: MP04AB1234

# Output:
# Valid Vehicle Number


vehicle = input("Enter vehicle number: ")

valid = True

if len(vehicle) == 10:
    for ch in vehicle[0:2]:
        if not ch.isalpha():
            valid = False
            break

    if valid:
        for ch in vehicle[2:4]:
            if not ch.isdigit():
                valid = False
                break

    if valid:
        for ch in vehicle[4:6]:
            if not ch.isalpha():
                valid = False
                break

    if valid:
        for ch in vehicle[6:10]:
            if not ch.isdigit():
                valid = False
                break
else:
    valid = False

if valid:
    print("Valid Vehicle Number")
else:
    print("Invalid Vehicle Number")