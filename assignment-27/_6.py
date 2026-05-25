# 6.
#  Advanced Student Registration Data Processing System

# A national university is developing an intelligent registration portal.
# Students enter registration codes using uppercase letters, lowercase
# letters, digits, and special symbols. Due to inconsistent data entry,
# the administration wants the system to standardize and process the
# information before storing it.

# Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
# alphabets and digits - Convert all alphabets to lowercase - Remove
# duplicate alphabets - Arrange alphabets in ascending order - Arrange
# digits in descending order - Display alphabets first and digits later -
# If no digits are found, display “No Digits Found”

# Test Case 1 Input: Enter registration code: zBc@638

# Output: Result: bcz863

# Test Case 2 Input: Enter registration code: 5Br$dE654b

# Output: Result: bder6554

# Test Case 3 Input: Enter registration code: A9@C3d#6B1a

# Output: Result: abcd9631

# Test Case 4 Input: Enter registration code: X#X@M2A4x7

# Output: Result: amx742

# Test Case 5 Input: Enter registration code: r@T#y

# Output: Result: rty No Digits Found

# ===================================================

code = input("Enter registration code: ")

alphabets = ""
digits = ""

for ch in code:
    if ch.isalpha():
        alphabets += ch.lower()
    elif ch.isdigit():
        digits += ch

# Remove duplicate alphabets
unique_alpha = ""
for ch in alphabets:
    if ch not in unique_alpha:
        unique_alpha += ch

# Sort alphabets ascending
alpha_sorted = ""
for i in range(97, 123):
    for ch in unique_alpha:
        if ord(ch) == i:
            alpha_sorted += ch

# Sort digits descending
digit_sorted = ""
for i in range(9, -1, -1):
    for ch in digits:
        if int(ch) == i:
            digit_sorted += ch

if digit_sorted == "":
    print("Result:", alpha_sorted)
    print("No Digits Found")
else:
    print("Result:", alpha_sorted + digit_sorted)