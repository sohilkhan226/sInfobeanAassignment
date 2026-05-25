# 1.
# Email Username Validator

# A company wants to check whether an employee email username is valid before creating an official account.

# Conditions:
# - Username should start with a letter
# - Username can contain letters, digits, underscore (_)
# - No spaces allowed
# - Length should be between 5 and 12 characters

# Input:
# Enter username: ajay_123

# Output:
# Valid Username

username = input("Enter username: ")

valid = True

# Check length
if len(username) < 5 or len(username) > 12:
    valid = False

# Check starts with letter
if valid and not username[0].isalpha():
    valid = False

# Check valid characters only
if valid:
    for ch in username:
        if not (ch.isalpha() or ch.isdigit() or ch == "_"):
            valid = False
            break

# Check no spaces
if valid:
    for ch in username:
        if ch == " ":
            valid = False
            break

if valid:
    print("Valid Username")
else:
    print("Invalid Username")










