# 5.
# Cybercrime Log Analysis System

# A cybersecurity company monitors encrypted login activity stored as character-based security logs.

# During investigation, analysts need to identify the last character that repeats in the log sequence.
# This helps detect the most recent duplicated activity pattern before a possible security breach.

# Write a Python program to find the last repeating character in a given string.

# If no repeating character exists, print:

# No repeating character found
# Input:
# abccdbefga
# Output:
# a


text = input("Enter string: ")

last_repeat = ""

for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j]:
            last_repeat = text[i]

if last_repeat == "":
    print("No repeating character found")
else:
    print("Last repeating character:", last_repeat)

