# 6.

# Product Code Verification System

# An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

# Conditions:
# - Ignore spaces
# - Ignore case sensitivity

# Input:
# Enter first product code: Dormitory
# Enter second product code: Dirty Room

# Output:
# Both Product Codes are Matching

code1 = input("Enter first product code: ")
code2 = input("Enter second product code: ")

# Remove spaces and convert to lowercase
clean1 = ""
clean2 = ""

for ch in code1:
    if ch != " ":
        clean1 += ch.lower()

for ch in code2:
    if ch != " ":
        clean2 += ch.lower()

# Count frequency of each character
if len(clean1) != len(clean2):
    print("Both Product Codes are Not Matching")
else:
    matched = True
    for ch in clean1:
        count1 = 0
        count2 = 0
        for c in clean1:
            if c == ch:
                count1 += 1
        for c in clean2:
            if c == ch:
                count2 += 1
        if count1 != count2:
            matched = False
            break

    if matched:
        print("Both Product Codes are Matching")
    else:
        print("Both Product Codes are Not Matching")
